<template>
  <div class="root_page">
    <router-view></router-view>
  </div>
</template>
<script setup>
import index_page from './index_page.vue';
import { ref, computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import login from './login_page/login.vue'
import register from './register_page/register.vue';
import { useRouter } from 'vue-router';
import { get_token, get_csrf_token, verify_token, refresh_token } from './auto_token_auth'


const store = useStore();
const router = useRouter();

let index_page_show = computed(() => store.getters.index_page_show);
let login_page_show = computed(() => store.getters.login_page_show);
let register_page_show = computed(() => store.getters.register_page_show);

onMounted(async () => {
  //获取token
  let token = localStorage.getItem('auth_token');
  let refresh_token_a = localStorage.getItem('refresh_token');
  let login_status = await verify_token(token);
  if (!login_status) {
    alert('登录已过期，请重新登录');
    router.push('/login');
    store.commit('set_login_status',false)
    return;
  }

  //刷新token
  let new_token = await refresh_token(refresh_token_a);
  if (new_token) {
    localStorage.setItem('auth_token', new_token); // 保存新的 token
    store.commit('set_login_status',true)
  } else {
    alert('Token refresh failed, please login again.');
    router.push('/login');
    store.commit('set_login_status',false)
  }


  let csrf_token = await get_csrf_token();
  localStorage.setItem('csrf_token', csrf_token);
  //设置csrf_token的cookie
  document.cookie = `csrf_token=${csrf_token};path=/;domain=localhost;`
  console.log(csrf_token);
})

//在页面新增一个不可见的div元素并点击一次，然后删除该元素
onMounted(() => {
  let div = document.createElement('div');
  div.style.display = 'none';
  document.body.appendChild(div);
  div.click();
  document.body.removeChild(div);
})

</script>

<style scoped></style>