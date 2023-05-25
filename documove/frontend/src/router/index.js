import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/movies/Home.vue'
import Community from '@/views/community/Community.vue'
import Login from '@/views/accounts/Login.vue'
import Signup from '@/views/accounts/Signup.vue'
import Recommend from '@/views/recommend/Recommend.vue'
import GivingTheme from '@/views/giving/GivingTheme.vue'
import GivingDetail from '@/views/giving/GivingDetail.vue'
import Giving from '@/views/giving/Giving.vue'
import MovieDetail from '@/components/movies/MovieDetail.vue'
import MyPage from '@/views/accounts/MyPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path:'/giving',
    name:'Giving',
    component: Giving
  },
  {
    path:'/givingdetail',
    name:'GivingDetail',
    component: GivingDetail
  },
  {
    path:'/givingtheme',
    name: 'GivingTheme',
    component: GivingTheme
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup/',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login/',
    name: 'Login',
    component: Login
  },
  {
    path: '/community/reviews/',
    name: 'Community',
    component: Community
  },
  {
    path: '/movie',
    name: 'MovieDetail',
    component: MovieDetail,
    props: true
  },
  {
    path: '/recommend/',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/mypage/:userId',
    name: 'MyPage',
    component: MyPage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
