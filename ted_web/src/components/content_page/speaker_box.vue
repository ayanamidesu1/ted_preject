<template>
    <div class="speaker_box">
        <div class="content">
            <div class="title">
                <span>关于演讲者</span>
            </div>
            <div class="speaker_info">
                <div class="info_box">
                    <div class="avatar">
                        <img :src="'http://localhost:8000/static/img/thumbnail/'+user_info.avatar_path+'.png'">
                    </div>
                    <div class="speaker_name">
                        <span style="font-size: 18px;font-weight:bold;">{{user_info.username }}</span>
                        <span style="font-size: 12px;color:rgb(133,133,133)">{{ user_info.user_tags }}</span>
                    </div>
                </div>
                <div class="speaker_intruduction">
                    <span>{{ user_info.introduce }}</span>
                </div>
            </div>
            <div class="speaker_self_website_list">
                <div class="website_box">
                    <div class="website_intruduction">
                        <span>{{user_info.self_website_introduce }}</span>
                    </div>
                    <div class="go_website">
                        <a :href="user_info.self_website" target="_blank">
                            <span>学习/了解&nbsp;→</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref,defineProps,defineEmits } from 'vue';
let speaker_info = ref({
    avatar: "src/assets/image/65014220_p0.jpg",
    title: '气候影响学者',
    name: "约翰·道格拉斯·克罗克福德",
    intruduction: "这是一段自我介绍",
    self_website: "https://localhost:10000",
    self_website_intruduction: "这是一段个人网站介绍",
})

let props = defineProps({
    user_info: Object
})
let user=ref(JSON.parse(localStorage.getItem('user')))

</script>

<style scoped>
.speaker_box {
    display: flex;
    flex-direction: column;
}

.content {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.title {
    font-size: 24px;
    font-weight: 700;
    border-bottom: 1px solid rgb(133, 133, 133);
}
.speaker_info{
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.info_box{
    gap:10px;
    display: flex;
    align-items: center;
}
.avatar{
    width:50px;
    height: 50px;
    display: flex;
}
.avatar img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}
.speaker_name{
    display: flex;
    flex-direction: column;
    gap:5px;
}
.speaker_intruduction{
    border-top: 1px solid rgb(133, 133, 133);
    display: flex;
    align-items: center;
}
.speaker_self_website_list{
    margin-top:20px;
    display: flex;
    flex-direction: column;
    gap:20px;
    border-top:1px solid rgb(133, 133, 133);
}
.website_box{
    margin-top: 10px;
    width: 90%;
    padding: 20px;
    display: flex;
    position: relative;
    background-color: rgba(133,133,133,0.5);
    border-radius: 10px;
    justify-content: space-between;
}
.website_intruduction{
    width: 80%;
    display: flex;
    align-items: center;
}
.go_website{
    width:calc(100% - 80% - 10px);
    display: flex;
    padding: 5px 15px;
    background-color: red;
    color: white;
    border-radius: 10px;
    justify-content: center;
    align-items: center;
    align-self: flex-end;
    font-size: 18px;
    font-weight: 700;
}
.go_website a{
    text-decoration: none;
    color: white;
}
</style>