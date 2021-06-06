import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

window.$ = window.jQuery = require('jquery')
createApp(App).use(router).mount('#app')
