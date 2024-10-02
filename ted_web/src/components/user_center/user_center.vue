<template>
  <div class="user_center" v-if="user_info">
    <div class="content">
        <background :user_info="user_info" v-if="background_ready"></background>
        {{ user_info }}
    </div>
  </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import get_all_user_info from './js/get_user_info';
import background from './background.vue';

const user_info = ref(null);
const background_ready = ref(false);

onMounted(async function(){
  user_info.value = await get_all_user_info();
  console.log(user_info.value);
  background_ready.value = true;
})

</script>

<style scoped>
  
</style>