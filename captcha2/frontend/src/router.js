import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('./views/Login')
    },
    {
      path: '/success',
      name: 'success',
      component: () => import('./views/Success')
    },
  ]
})

export default router
