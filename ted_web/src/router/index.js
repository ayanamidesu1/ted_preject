import { createRouter, createWebHistory } from 'vue-router'
import index_recommend from '../components/index_com/index_recommend.vue'
import content_page from '../components/content_page/content_page.vue'
import login from '../components/login_page/login.vue'
import register from '../components/register_page/register.vue'
import root from '../components/root.vue'
import index_page from '../components/index_page.vue'

const routes = [
  {
    path: '/',
    component: root,
    children: [
      {
        path: '',  // 默认加载的子路由，当路径为 / 时，显示 index_page
        component: index_page,
        children: [
          {
            path: '',  // 当路径为 / 时显示推荐页面
            component: index_recommend
          },
          {
            path: 'content_page',
            name: 'content_page',
            component: content_page
          }
        ]
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },
  {
    path: '/register',
    name: 'register',
    component: register
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
