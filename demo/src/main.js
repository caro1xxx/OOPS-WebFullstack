import Vue from 'vue'
import App from './App.vue'
import router from './router' // 加载router
import store from './store'  // 加载vuex
import $ from 'jquery'  // 加载jquery
// import 'bootstrap'   // 加载bootstrap  这里引入的话会导致一些功能不能正常使用
import 'bootstrap/dist/js/bootstrap.min.js' // 引入bootstrap样式
import 'bootstrap/dist/css/bootstrap.min.css' // 引入bootstrap样式

import '../src/assets/css/App.css'  
import axios from 'axios'

import VueCookies from 'vue-cookies'

Vue.use(VueCookies)

Vue.config.productionTip = false
Vue.prototype.$=$
Vue.prototype.$axios = axios;


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
