import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path:'/more/:id',
    name:'More',
    component:() => import('../views/More.vue')
  },
  {
    path: '/user',
    name: 'User',
    component: () => import('../views/User.vue')
  },
  {
    path: '/signin',
    name: 'Signin',
    component: () => import('../views/Signin.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/donation',
    name: 'Donation',
    component: () => import('../views/Donation.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/click/:id',
    name: 'Click',
    component: () => import('../views/Click.vue')
  },
  {
    path: '/click2/:id',
    name: 'Click2',
    component: () => import('../views/Click2.vue')
  },
  {
    path: '/agreement',
    name: 'Agreement',
    component: () => import('../views/Agreement.vue')
  },
  {
    path: '/news/:id',
    name: 'News',
    component: () => import('../views/News.vue')
  },
  {
    path: '/forget',
    name: 'Forget',
    component: () => import('../views/Forget.vue')
  },
  {
    path: '/search/:iS',
    name: 'Search',
    component: () => import('../views/Search.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
