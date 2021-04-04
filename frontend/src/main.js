import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import 'normalize.css'

import VueProgressBar from 'vue-progressbar'

import App from './App.vue'
import store from './store'
import router from './router'
// import store from './store'
import {library} from '@fortawesome/fontawesome-svg-core'
import {
    faAddressCard,
    faAlignLeft,
    faAsterisk,
    faBackward,
    faBox,
    faCloud,
    faCoffee,
    faEye,
    faPowerOff,
    faServer,
    faSpinner,
    faUserCircle,
    faWrench,
} from '@fortawesome/free-solid-svg-icons'

import {faTelegram} from '@fortawesome/free-brands-svg-icons'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import ECharts from 'vue-echarts'
import service from '@/utils/request'
import '@/styles/index.scss' // global css

library.add(faSpinner, faAlignLeft)
library.add(faBox, faEye, faCoffee, faUserCircle, faPowerOff, faAddressCard, faWrench, faBackward, faAsterisk, faServer, faCloud,);
library.add(faTelegram);

// Vue.config.devtools = true
Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.use(VueProgressBar, {
    color: 'rgb(143, 255, 199)',
    failedColor: 'red',
    height: '2px'
})

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('echarts', ECharts)

// if the table component cannot access `this.$axios`, it cannot send request
Vue.prototype.$axios = service
// 注册全局事件总线
Vue.prototype.$eventBus = new Vue()

new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
})

