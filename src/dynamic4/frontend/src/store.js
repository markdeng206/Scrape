import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    url: {
      index: '/api/news',
      detail: '/api/news/{id}'
    }
  },
  mutations: {

  },
  actions: {

  }
})
