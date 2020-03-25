import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import './plugins/element.js'
import './assets/scss/theme.scss'
import './assets/scss/style.scss'
import './assets/scss/round.scss'
import './assets/scss/pm.scss'
import store from './store'
import router from './router'
import moment from 'moment'

Vue.config.productionTip = false


new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
