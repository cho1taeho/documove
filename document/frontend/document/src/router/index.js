import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'
import DetailView from '@/views/DetailView'
import MyPageView from '@/views/MyPageView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path:'/create',
    name:'CreateView',
    component: CreateView
  },
  {
    path:'/login',
    name: 'LogInView',
    component:LogInView
  },
  {
    path:'/singup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView
  },
  {
    path:'/mypage',
    name: 'MyPageView',
    component: MyPageView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
