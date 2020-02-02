import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    url: {
      root: '/',
      login: '/api/login',
      init: '/api/init'
    }
  }
})
