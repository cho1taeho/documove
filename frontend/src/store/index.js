import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

const SERVER_URL = 'http://127.0.0.1:8000/'
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_KEY = process.env.VUE_APP_YOUTUBE_API

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    token:'',
    username:'',
    selectedThemeID: null,
    showThemeSelection: false,
    selectedTheme: '',
    // accounts
    isLogin: false,
    // movies
    movies: [],
    genre_names: [],
    // community
    reviews: [],
    reviewDetail: null,
    movieTitles: [],
    comments: [],
    comment: null,
    // tinder
    randomMovies: [],
    genres: [],
    // recommend
    recommendMovies: [],
    bestGenre: null,
    // youtube
    youtubeVideos: [],
    userPoints: 0,
    givings:[],
    user: null,
    wishlist: null,
  },
  getters: {    
    themeGivings: state => {     
      if (!state.selectedTheme) {
        return state.givings
      }
      return state.givings.filter(giving => giving.themes.theme[0].id === state.selectedTheme)
    },
    givings(state) {
      return state.givings
    },
    getUserPoints(state) {
      return state.userPoints
    },
    movies(state) {
      return state.movies
    },
    movieTitles(state) {
      return state.movieTitles
    },
    reviews(state) {
      return state.reviews
    },
    comments(state) {
      return state.comments
    },
    randomMovies(state) {
      return state.randomMovies
    },
    genres(state) {
      return state.genres
    },
    genre_names(state) {
      return state.genre_names
    },
    recommendMovies(state) {
      return state.recommendMovies
    },
    bestGenre(state) {
      return state.bestGenre
    },
    topDonator(state) {
      return state.topDonator
    }
  },
  mutations: {
    SET_MOVIE_DETAILS(state, movie) {
      state.movieDetail = movie
    },
    SET_ISAUTHENTICATED(state, payload) {
      state.isAuthenticated = payload
    },
    SET_TOKEN(state, payload) {
      state.token = payload
    },
    SET_USERNAME(state, payload) {
      state.username = payload
    },
    SET_SELECTEDTHEMEID(state, payload) {
      state.selectedThemeID = payload
    },
    setGivings(state, givings) {
      state.givings = givings
    },
    toggleThemeSelection(state) {
      state.showThemeSelection = !state.showThemeSelection
    },
    setSelectedTheme(state, theme) {
      state.selectedTheme = theme
    },
    GET_GIVINGS(state, givings) {
      state.givings= givings
    },
    updataUserPoints(state, points) {
      state.userPoints = points
    },
    // ACCOUNTS MUTATIONS
    SET_USER(state, user) {
      state.user = user
    },
    SET_WISHLIST(state, wishlist) {
      state.wishlist = wishlist
    },
    LOGIN(state) {
      state.isLogin = true
    },
    LOGOUT(state) {
      state.isLogin = false
    },
    // MOVIES MUTATIONS
    GET_MOVIES(state, res) {
      state.movies = res
    },
    GET_MOVIE_TITLES(state, res) {
      const tmp_list = []
      for (var value of res) {
        const tmp = {
          name: value.title, value: value.title
        }
        tmp_list.push(tmp)
      }
      state.movieTitles = tmp_list
    },
    GET_GENRES(state, res) {
      state.genre_names = res
    },
    // COMMUNITY MUTATIONS
    GET_REVIEWS(state, res) {
      state.reviews = res
    },
    CREATE_REVIEW(state, res) {
      state.reviews.push(res)
    },
    UPDATE_REVIEW(state, reviewItem) {
      state.reviews = state.reviews.map((review) => {
        if (review === reviewItem) {
          return { ...review,
            title: reviewItem.title,
            content: reviewItem.content,
            rank: reviewItem.rank,
          }
        }
        return review
      })
    },
    DELETE_REVIEW(state, reviewItem) {
      const index = state.reviews.indexOf(reviewItem)
      state.reviews.splice(index, 1)
    },
    CREATE_COMMENT(state, res) {
      state.comments.push(res)
    },
    READ_COMMENT(state, res) {
      state.comment = res
    },
    UPDATE_COMMENT(state, commentItem) {
      state.comments = state.comments.map((comment) => {
        if (comment === commentItem) {
          return { ...comment, content: commentItem.content }
        }
        return comment
      })
    },
    DELETE_COMMENT(state, commentItem) {
      const index = state.comments.indexOf(commentItem)
      state.comments.splice(index, 1)
    },
    GET_COMMENTS(state, res) {
      state.comments = res
    },
    SUBMIT_GENRES() {
      // 임시로 놔둠
    },
    // RECOMMEND MUTATIONS
    GET_LIKE_GENRE_MOVIES(state, res) {
      state.recommendMovies = res.data
      state.bestGenre = res.best_genre
    },
    // YOUTUBE MUTATIONS
    SEARCH_YOUTUBE: function (state, res) {
      state.youtubeVideos = res.data.items
    },
    SET_TOP_DONATOR(state, topDonator) {
      state.topDonator = topDonator
    },
  },
  actions: {
    async getMovieDetails({ commit }, id) {
      try {
        const response = await axios.get(`${SERVER_URL}movies/${id}`);
        const movie = response.data;
        commit('SET_MOVIE_DETAILS', movie);
      } catch (error) {
        console.log(error);
      }
    },
    setTheme({ commit }, theme) {
      commit('setSelectedTheme', theme)
    },
    selectTheme({commit}, theme) {
      commit('setSelectedTheme', theme)
    },
   
    async getGivings({ commit }) {
      try {
        const response = await axios.get(`${SERVER_URL}movies/giving/`);
        const givings = response.data;
        commit('GET_GIVINGS', givings);
      } catch (error) {
        console.log(error);
      }
    },
    fetchUserPoints({commit}) {
      axios
        .get('/api/user/points')
        .then(response => {
          const points = response.data.points
          commit('updateUserPoints', points)
        })
    },
    setSelectedThemeID({commit}, selectedThemeID) {
      commit('SET_SELECTEDTHEMEID', selectedThemeID)
    },
    // ACCOUNTS ACTIONS
    login({commit}, credentials) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}accounts/api-token-auth/`,
        data: credentials,
      })
      .then(res => {
        localStorage.setItem('jwt', res.data.token)
        commit('LOGIN')
        const selectedThemeID= res.data.selectedThemeID
        commit('SET_ISAUTHENTICATED', true); 
        commit('SET_SELECTEDTHEMEID', selectedThemeID);
        router.push({name: 'Home'})
      })
      .catch(err => console.log(err))
      
    },
    checkLogin({commit}, token) {
      if (token) {
        commit('LOGIN')
      }
    },
    logout({commit}) {
      localStorage.removeItem('jwt')
      commit('LOGOUT')
      router.push({ name: 'Login' })
    },
    // MOVIES ACTIONS
    getMovies({commit}, token) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/`,
        headers: token,
      })
      .then(res => {
        commit('GET_MOVIES', res.data)
        commit('GET_MOVIE_TITLES', res.data)
      })
      .catch(err => console.log(err))
    },
    getGenres({commit}, token) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/genres/`,
        headers: token
      })
      .then((res) => {
        commit('GET_GENRES', res.data)
      })
      .catch(err => console.log(err))
    },
    // COMMUNITY - REVIEW ACTIONS
    getReviews({commit}, token) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}community/reviews/`,
        headers: token,
      })
      .then(res => {
        commit('GET_REVIEWS', res.data)
      })
      .catch(err => console.log(err))
    },
    createReview({commit}, objs) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}community/reviews/`,
        data: objs.reviewItem,
        headers: objs.token
      })
      .then(() => {
        commit('CREATE_REVIEW')
        router.push({name: 'Community'})
        router.go()
      })
      .catch(err => console.log(err))
    },
    updateReview({commit}, objs) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}community/reviews/${objs.review_id}/`,
        data: objs.reviewItem,
        headers: objs.token
      })
      .then(() => {
        commit('UPDATE_REVIEW')
      })
      .catch(err => console.log(err))
    },
    deleteReview({commit}, objs) {
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}community/reviews/${objs.review_id}/`,
        headers: objs.token
      })
      .then(() => {
        commit('DELETE_REVIEW')
        router.go()
      })
      .catch(err => console.log(err))
    },
    // COMMUNITY - COMMENT ACTIONS
    getComments({commit}, objs) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}community/reviews/${objs.review_id}/comments/`,
        headers: objs.token
      })
      .then((res) => {
        commit('GET_COMMENTS', res.data)
      })
      .catch(err => console.log(err))
    },
    createComment({commit}, objs) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}community/reviews/${objs.review_id}/comments/`,
        data: objs.commentItem,
        headers: objs.token
      })
      .then((res) => {
        commit('CREATE_COMMENT', res.data)
      })
      .catch(err => console.log(err))
    },
    readComment({commit}, objs) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}community/comments/${objs.comment_id}/`,
        headers: objs.token
      })
      .then((res) => {
        commit('READ_COMMENT', res.data)
      })
      .catch(err => console.log(err))
    },
    updateComment({commit}, objs) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}community/comments/${objs.comment_id}/`,
        data: objs.commentItem,
        headers: objs.token
      })
      .then((res) => {
        commit('UPDATE_COMMENT', res.data)
      })
      .catch(err => console.log(err))
    },
    deleteComment({commit}, objs) {
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}community/comments/${objs.comment_id}/`,
        headers: objs.token
      })
      .then((res) => {
        commit('DELETE_COMMENT', res.data)
      })
      .catch(err => console.log(err))
    },
    // RECOMMEND ACTIONS
    getLikeGenreMovies({commit}, token) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/recommend/`,
        headers: token,
      })
      .then((res) => {
        commit('GET_LIKE_GENRE_MOVIES', res.data)
      })
      .catch(err => console.log(err))
    },
    async fetchTopDonator({ commit }) {
      try {
        const response = await axios.get('/api/top-donator')
        const topDonator = response.data
        commit('SET_TOP_DONATOR', topDonator)
      } catch (error) {
        console.error(error)
      }
    },
  },
  modules: {

  },
})
