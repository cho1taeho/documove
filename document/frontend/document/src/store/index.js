import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

import jwt from 'jsonwebtoken'

// import { currentRoute } from 'vue-router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [],    
    token: null,
    isLoggedIn: false, 
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    isLoggedIn(state) { 
      return state.isLoggedIn
    },
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      state.isLoggedIn = true 
    },
    CLEAR_TOKEN(state) {
      state.token = null
      state.isLoggedIn = false // 추가: 로그인 상태를 false로 설정
    },
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
        //   Authorization: context.state.token ? `Token ${context.state.token}` : undefined,
        },
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getMypage(context) {
      axios({
        methods: 'get',
        url: `${API_URL}/api/v1/articles/:id`,
        headers: {
          Authorization: context.state.token ? 
        }
      })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          router.push('/login')
        })
        .catch((err) => {
          if (err.response && err.response.wlsstatus === 400 && err.response.data.username) {
            alert('아이디 중복')
          } else {
            console.log(err)
          }
        })
    },
   
    async login(context, payload) {
      const username = payload.username
      const password = payload.password
    
      try {
        const res = await axios.post(`${API_URL}/accounts/login/`, {
          username,
          password,
        })
        const token = res.data.key
        context.commit('SAVE_TOKEN', token)
        router.push({ name: 'ArticleView' }) 
        jwt.verify()       
      } catch (err) {
        console.log(err)
        alert('비번틀림')
        return
      }
    },
    logout(context) {
      context.commit('CLEAR_TOKEN')
      router.push({ name: 'ArticleView' })
    },
   
  },
  modules: {},
})