import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

// import jwt from 'jsonwebtoken'

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
    point : 0,
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
      state.isLoggedIn = false 
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
<<<<<<< HEAD
    // getMypage(context) {
    //   axios({
    //     methods: 'get',
    //     url: `${API_URL}/api/v1/articles/:id`,
    //     headers: {
    //       Authorization: context.state.token ? 
    //     }
    //   })
    // },
=======
>>>>>>> 65d05107cd29100d85e1147a4192afdd9bddf8cd
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
<<<<<<< HEAD
        // jwt.verify()       
=======
     
>>>>>>> 65d05107cd29100d85e1147a4192afdd9bddf8cd
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
      // axios
      //   .post(`${API_URL}/accounts/api/points/increase/`, null, {
      //     headers: {
      //       Authorization: `Token ${context.state.token}`,
      //     },
      //   })
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