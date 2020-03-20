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

Vue.config.productionTip = false

import VueMoment from 'vue-moment'
import moment from 'moment-timezone'

Vue.use(VueMoment, {
  moment,
})
new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
