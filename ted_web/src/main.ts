import { createApp } from 'vue'
import App from './App.vue'
import store from './store.js'
import { RootState, Mutation } from './store.d';
import router from './router'

const app= createApp(App)
const DEBOUNCE_TIME = 50;
// 订阅器，用于监听页面状态的变化
store.subscribe((mutation: Mutation, state: RootState) => {
    if (mutation.type === 'SET_PAGESTATUS' || 
        mutation.type === 'SET_CONTENT_PAGE' || 
        mutation.type === 'SET_SINGLE_PAGE_STATUS' ||
        mutation.type === 'SET_INDEX_PAGE'
    ) {
      if (state.pushTimer) {
        clearTimeout(state.pushTimer); // 清除之前的定时器
      }
      state.pushTimer = setTimeout(() => {
        state.pushTimer = null;
        store.commit('PUSH_PAGE_STATE'); // 在页面状态改变时记录状态
      }, DEBOUNCE_TIME);
    }
  });

app.use(router)
app.use(store)
app.mount('#app')
