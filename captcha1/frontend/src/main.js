import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import router from './router'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import store from './store'
import './assets/scss/theme.scss'
import './assets/scss/style.scss'
import './assets/scss/round.scss'
import './assets/scss/pm.scss'

require('@/assets/js/geetest.js');

Vue.use(VueAxios, axios)

Vue.use(ElementUI)

Vue.config.productionTip = false

Vue.prototype.$initGeet = initGeetest

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
