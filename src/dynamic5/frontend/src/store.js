import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    url: {
      index: '/api/book',
      detail: '/api/book/{id}',
      proxy: '/proxy/{url}'
    }
  },
  mutations: {},
  actions: {}
})
