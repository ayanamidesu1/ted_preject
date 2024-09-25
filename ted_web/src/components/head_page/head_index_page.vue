<template>
  <div class="head_index_page">
    <div class="content">
      <div class="home_box">
        <div class="home_btn">
          <router-link to="/" style="text-decoration: none; color: inherit;">
            <span>主页</span>
          </router-link>
        </div>
        <div class="home_tips">
          <span>多想想，或许改变一切</span>
        </div>
      </div>
      <div class="lable_box">
        <div class="lable_item lable_item_hover">
          <span>看</span>
          <div class="lable_item_dropdown">
            <span>演讲</span>
            <span>播放列表</span>
            <span>系列</span>
            <span>视频</span>
          </div>
        </div>
        <div class="lable_item lable_item_hover">
          <span>发现</span>
          <div class="lable_item_dropdown">
            <span>项目1</span>
            <span>项目2</span>
            <span>项目3</span>
            <span>项目4</span>
          </div>
        </div>
        <div class="lable_item lable_item_hover">
          <span>出席</span>
          <div class="lable_item_dropdown">
            <span>项目1</span>
            <span>项目2</span>
            <span>项目3</span>
            <span>项目4</span>
          </div>
        </div>
        <div class="lable_item lable_item_hover">
          <span>参与</span>
          <div class="lable_item_dropdown">
            <span>项目1</span>
            <span>项目2</span>
            <span>项目3</span>
            <span>项目4</span>
          </div>
        </div>
        <div class="lable_item lable_item_hover">
          <span @click="show_login_page">登录</span>
        </div>
        <div class="lable_item lable_item_hover">
          <span @click="show_register_page()">注册</span>
        </div>
        <div class="search_box">
          <div class="search_btn" @click="search_input_box_show = !search_input_box_show">
            <img src="../../assets/svg/搜索.svg" alt="搜索" class="icon">
          </div>
          <div class="search_input_box" :class="search_input_box_show ? 'search_input_box_show' : ''">
            <input type="text" placeholder="搜索" v-model="search_key">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore()
const router = useRouter()

let search_key = ref('')
let search_input_box_show = ref(false)

//展开登录页面
function show_login_page() {
  //store.commit('SET_SINGLE_PAGE_STATUS',{'key':'login_page_show','value':true})
  router.push('/login')
}
//展开注册页面
function show_register_page() {
  //store.commit('SET_SINGLE_PAGE_STATUS',{'key':'register_page_show','value':true})
  router.push('/register')
}

</script>

<style scoped>
.icon {
  width: 25px;
  height: 25px;
  object-fit: cover;
}

.head_index_page {
  width: 100%;
  height: 80px;
  display: flex;
  border-bottom: 2px solid rgb(133, 133, 133);
  align-items: center;
}

.content {
  width: 100%;
  height: 100%;
  display: flex;
  gap: 10px;
  align-items: center;
  justify-content: space-between;
}

.home_box {
  width: auto;
  height: 100%;
  display: flex;
  gap: 10px;
  align-items: center;
  position: relative;
}

.home_btn {
  width: auto;
  height: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(188, 12, 12, 1);
  font-size: 42px;
  font-weight: 700;
  cursor: pointer;
  margin-left: 20px;
}

.home_btn:hover {
  opacity: 0.8;
  transform: scale(1.05);
  transition: all 0.2s ease-in-out;
}

.home_tips {
  color: rgba(133, 133, 133, 1);
}

.lable_box {
  width: auto;
  height: 30px;
  display: flex;
  gap: 10px;
  font-weight: 600;
  position: relative;
  z-index: 10;
}

.lable_item {
  width: auto;
  height: auto;
  display: flex;
  position: relative;
  cursor: pointer;
  padding: 10px 15px;
  border-radius: 5px;
  justify-content: center;
  align-items: center;
}

.lable_item:hover .lable_item_dropdown {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.lable_item_hover:hover {
  transform: scale(1.01);
  transition: all 0.2s ease-in-out;
  background-color: rgb(133, 133, 133);
}

.lable_item_dropdown {
  width: 200px;
  height: auto;
  display: flex;
  flex-direction: column;
  gap: 10px;
  position: absolute;
  top: calc(100% + 10px);
  left: -80px;
  opacity: 0;
  visibility: hidden;
  border-radius: 10px;
  border: 1px solid rgba(133, 133, 133, 1);
  background-color: white;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease-in-out;
  transform: translateY(-20px);

}

.lable_item_dropdown span {
  padding: 10px;
  color: rgba(0, 0, 0, 0.7);
}

.lable_item_dropdown span:hover {
  background-color: rgba(0, 0, 0, 0.05);
}

.search_box {
  width: auto;
  height: 35px;
  display: flex;
  position: relative;
  justify-content: center;
  align-items: center;
  margin-right: 10px;
}

.search_btn {
  width: auto;
  height: auto;
  display: flex;
  cursor: pointer;
  border-radius: 50%;
  padding: 10px;
}

.search_btn:hover {
  background-color: rgba(170, 170, 170, 0.5);
  transition: all 0.3s ease-in-out;
}

.search_input_box {
  position: absolute;
  top: 0;
  right: calc(100% + 10px);
  width: 0;
  height: 35px;
  overflow: hidden;
  display: flex;
  align-items: center;
  background-color: white;
  border: 1px solid rgba(133, 133, 133, 1);
  border-radius: 5px;
  transition: all 0.3s ease-in-out;
}

.search_input_box input {
  width: 100%;
  padding: 0 10px;
  border: none;
  outline: none;
}

.search_input_box_show {
  width: 400px;
  transition: all 0.3s ease-in-out;
}
</style>
