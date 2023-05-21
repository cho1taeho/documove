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
    articles: [],    
    token: null,
    // isLoggedIn: false, 
    point : 0,
    isRegistered: false,
    inputShow: false,
  },
  getters: {
    isLogin(state) {
      // return state.token ? true : false
      return state.token !== null && !state.isRegistered
    },
    // isLoggedIn(state) { 
    //   return state.isLoggedIn
    // },
    isSingUp() {
      return this.$route.name === 'SignUpView'
    }
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
      state.isLoggedIn = false 
    },
    SET_REGISTERED(state, status) {
      state. isRegistered = status
    },
    SET_POINT(state, point) {
      state.point = point
    },
    SET_INPUT_SHOW(state, inputShow) {
      state.inputShow = inputShow
    }
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
          context.commit('SET_REGISTERED', true)
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
        context.commit('SET_REGISTERED', false)
        router.push({ name: 'ArticleView' }) 
     
      } catch (err) {
        console.log(err)
        alert('비밀번호가 일치하지 않습니다.')
        return
      }
    },
    logout(context) {
      context.commit('CLEAR_TOKEN')
      router.push({ name: 'ArticleView' })
    },
    increasePoints(context) {   
      axios({
        method : 'post',
        url : `${API_URL}/accounts/api/points/increase/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
        },
      })
        .then((response) => {
          context.commit('SET_POINT', response.data.points);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    showInputDialog(context) {
      context.commit('SET_INPUT_SHOW', true);
    },
    submitInput(context) {
      const pointsToReduce = parseInt(context.state.inputValue);
      if (!isNaN(pointsToReduce) && pointsToReduce > 0 && pointsToReduce <= context.state.point) {
        axios({
          method: 'post',
          url : `${API_URL}/accounts/api/points/reduce/`,
          headers: {
            Authorization: `Token ${context.state.token}`,
          },

        })
          // .post(`${API_URL}/api/points/reduce/`, { points: pointsToReduce }, {
          //   headers: {
          //     Authorization: `Token ${context.state.token}`,
          //   },
          // })
          .then((response) => {
            context.commit('SET_POINT', response.data.points);
          })
          .catch((error) => {
            console.log(error);
          });
      } else if (pointsToReduce > context.state.point) {
        alert('Points are not enough.');
      }
      context.commit('SET_INPUT_SHOW', false);
      context.commit('SET_INPUT_VALUE', 0);
    },
  },
  modules: {},
})