import Vue from 'vue'
import VueRouter from 'vue-router'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import LogInView from '@/views/LogInView'
import SignUpView from '@/views/SignUpView'
import DetailView from '@/views/DetailView'
import MyPageView from '@/views/MyPageView'
import NavBar from '@/components/NavBar' 

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'ArticleView',
    components: {
      default: ArticleView,
      navbar: NavBar 
    }
  },
  {
    path: '/create',
    name: 'CreateView',
    components: {
      default: CreateView,
      navbar: NavBar
    }
  },
  {
    path: '/login',
    name: 'LogInView',
    components: {
      default: LogInView,
      navbar: NavBar
    }
  },
  {
    path: '/signup',
    name: 'SignUpView',
    components: {
      default: SignUpView,
      navbar: NavBar
    }
  },
  {
    path: '/detail/:id',
    name: 'DetailView',
    components: {
      default: DetailView,
      navbar: NavBar
    }
  },
  {
    path: '/mypage',
    name: 'MyPageView',
    components: {
      default: MyPageView,
      navbar: NavBar
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router