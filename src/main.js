import { createApp } from 'vue'
import router from '../src/routers'
import App from './App.vue'

createApp(App)
  .use(router)
  .mount('#app')