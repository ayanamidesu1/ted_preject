<template>
  <div class="root_page">
    <router-view></router-view>
  </div>
</template>
<script setup>
import index_page from './index_page.vue';
import { ref ,computed,onMounted} from 'vue';
import { useStore } from 'vuex';
import login from './login_page/login.vue'
import register from './register_page/register.vue';
import { useRoute } from 'vue-router';
import {get_token} from './auto_token_auth'

const store = useStore();
const router = useRoute();

let index_page_show = computed(()=>store.getters.index_page_show);
let login_page_show = computed(()=>store.getters.login_page_show);
let register_page_show = computed(()=>store.getters.register_page_show);

onMounted(async ()=>{
  let token=await get_token('test_user','123456');
  console.log(token);
})

</script>

<style scoped>
  
</style>