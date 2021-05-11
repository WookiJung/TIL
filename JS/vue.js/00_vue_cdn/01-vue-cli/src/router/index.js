import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Lunch from '@/views/Lunch.vue'

Vue.use(VueRouter)

const routes = [
  // '/', App <=> Parent <=> Child
  // '/lotto', lotto 추첨
  // '/lunch', lunch 추첨
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/lunch',
    name: 'Lunch',
    component:Lunch
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
