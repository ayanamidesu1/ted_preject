<template>
  <div class="background">
    <div class="content">
        <div class="background_img">
            <img :src="'http://localhost:8000/static/img/img/102718099_p0.jpg'" alt="背景">
        </div>
        <div class="user_box">
            <div class="avatar">
                <img :src="'http://localhost:8000/static/img/thumbnail/'+data.avatar_path+'.png'">
                <div class="edit_avatar">
                    <img src="http://localhost:8000/static/svg/图像.svg" alt="编辑头像">
                    <span>编辑头像</span>
                </div>
            </div>
            <div class="user_info">
                <div class="username">
                    <input v-model="data.username" type="text" placeholder="用户名">
                    <div class="edit_info_box">
                        <img src="http://localhost:8000/static/svg/编辑.svg" alt="编辑" class="icon">
                    </div>
                </div>
                <div class="user_tags">
                    <span>{{data.user_tags}}</span>
                </div>
            </div>
            <div class="self_website">
                <div class="website">
                    <span>{{data.self_website}}</span>
                </div>
                <div class="self_website_introduce">
                    <span>{{data.self_website_introduce}}</span>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>
<script setup>
import { ref,defineProps,computed } from 'vue'

let props = defineProps({
    user_info:Object
})
let data=computed(()=>(props.user_info.data.user_info))

</script>

<style scoped>
.icon{
    width:25px;
    height: 25px;
    object-fit: cover;
}
.content{
    width: 100%;
    height: 100%;
    display: flex;
    position: relative;
}
.background_img{
    width: 100%;
    height: 25%;
    display: flex;
}
.background_img img{
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.user_box{
    width: auto;
    height: 100px;
    display: flex;
    position:absolute;
    left: 10px;
    bottom: 10px;
    gap:10px;
    background-color: rgba(255, 255, 255, 0.7);
    padding: 10px 20px;
    border-radius: 15px;
}
.avatar{
    width: 100px;
    height: 100px;
    display: flex;
    position: relative;
    overflow: hidden;
    border-radius: 50%;
}
.avatar img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}
.edit_avatar{
    width: 100%;
    height: 100%;
    position: absolute;
    top:0;
    left: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.5);
    opacity: 0;
    transition: all 0.2s ease-in-out;
    cursor: pointer;
}
.edit_avatar:hover{
    opacity: 1;
    transform: scale(1.05);
    transform: translateY(-1px);
}
.edit_avatar img{
    width: 30px;
    height: 30px;
    object-fit: cover;
    border-radius: 0;
}
.user_info{
    display: flex;
    flex-direction: column;
    gap:5px;
    justify-content: space-around;
    max-width: 200px;
    overflow: hidden;
}
.username{
    display: flex;
    gap:5px;
    width: auto;
}
.self_website{
    display: flex;
    flex-direction: column;
    gap:5px;
    justify-content: space-around;
    max-width: 300px;
    overflow: hidden;
}
.user_box input{
    border: none;
    outline: none;
    background: none;
    font-size: 16px;
    width: calc(100% - 25px);
}
</style>