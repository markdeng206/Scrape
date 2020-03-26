import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'index',
      component: () => import('./views/Index.vue')
    },
    {
      path: '/page/:page',
      name: 'indexPage',
      component: () => import('./views/Index.vue')
    },
    {
      path: '/detail/:key',
      name: 'detail',
      component: () => import('./views/Detail.vue')
    }
  ]
})
