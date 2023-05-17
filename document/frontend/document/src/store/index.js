import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],  
  state: {
    articles: [  
    ],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'ArticleView'})
    }    
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
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
        url:`${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
      })
    },
    // login(context, payload) {
    //   const username = payload.username
    //   const password = payload.password

    //   axios({
    //     method: 'post',
    //     url: `${API_URL}/accounts/login/`,
    //     data: {
    //       username, password
    //     }
    //   })
    //     .then((res) => {
    //       context.commit('SAVE_TOKEN', res.data.key)
    //     })
    //   .catch((err) => console.log(err))
    // }
    async login(context, payload) {
      const username = this.username
      const password = this.password
  
      const payload = {
        username, password
      }
  
      try {
        await this.$store.dispatch('login', payload)
        this.$router.push('articles')
      } catch (err) {
        alert('아이디나 비밀번호가 잘못되었습니다.')
        console.log(err)
        this.$router.push('login')
      }
    }

  },
  modules: {
  }
})
