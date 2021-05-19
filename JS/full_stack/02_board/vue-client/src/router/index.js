import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'

import CreateView from '@/views/articles/CreateView.vue'
import ListView from '@/views/articles/ListView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/accounts/logout',
    name: 'Logout',
    component: LogoutView
  },
  // articles
  {
    path: '/articles',
    name: 'List',
    component: ListView
  },
  {
    path: '/articles/create',
    name: 'Create',
    component: CreateView
  },
]
  

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


// beforeEach는 router 경로 가기전에 항상 실행됨
// 인자는 차례대로 to, from, next가 온다
router.beforeEach((to, from, next) =>{
  console.log(to.name)
  // 로그인 해야만 함
  const privatePages=['Logout', 'Create']
  // 로그인 안해야만 가능
  const outerPages = ['Signup', 'Login']

  const isAuthRequired = privatePages.includes(to.name)
  const guestRequired = outerPages.includes(to.name)
  const isLoggedIn = store.getters.isLoggedIn

  // 로그인 사용자는 차단
  if (guestRequired && isLoggedIn) {
    next({name:'List'})
  }
  // 로그인 안한사용자는 차단.
  // if (isAuthRequired && !isLoggedIn) {
  //   next({name:'Login'})
  // } else {
  //   next()
  // }
  isAuthRequired && !isLoggedIn ? next({name:'Login'}) : next()

  if (!to.name) // 등록되지 않은 라우터는 to.name이 없음!
  { 
    next({name:'List'})
  }
})

export default router
