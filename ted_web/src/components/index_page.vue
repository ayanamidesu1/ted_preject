<script setup lang="ts">
import { ref } from 'vue'
import head_index_page from './head_page/head_index_page.vue';
import { useStore } from 'vuex'
import index_recommend from './index_com/index_recommend.vue';
import { useRoute } from 'vue-router'

const store = useStore()
const route = useRoute()

const count = ref(0)
</script>

<template>
  
  <div class="index_page">
    <head_index_page />
    <router-view></router-view>
  </div>

</template>

<style scoped></style>
