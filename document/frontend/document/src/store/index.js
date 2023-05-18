import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

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
    isLoggedIn: false, // 추가: 로그인 상태 여부를 저장하는 상태
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    isLoggedIn(state) { // 추가: 로그인 상태를 반환하는 getter
      return state.isLoggedIn
    },
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      state.isLoggedIn = true // 추가: 로그인 상태를 true로 설정
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
        
      } catch (err) {
        console.log(err)
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