<template>
    <div class="content_page">
        <div class="content">
            <div class="video_info">
                <div class="video_box">
                    <!-- 主视频播放器 -->
                    <video class="main-video" controls :src="video_path" @timeupdate="updateMainVideoTime"></video>
                    <div class="info_item">
                        <div class="main_video_tite">
                            {{main_video_title}}
                        </div>
                        <div class="main_video_data">
                            <span>{{main_video_info.watch_count}}次观看</span>|
                            <span>{{main_video_info.speaker}}</span>|
                            <span>{{main_video_info.speaker_intruduction}}</span>|
                            <span>{{main_video_info.create_time}}</span>
                        </div>
                        <div class="interaction_box">
                            <div class="share_btn interaction_btn">
                                <img class="icon" src="../../assets/svg/分享.svg" alt="分享">
                                <span>分享</span>
                            </div>
                            <div class="collect_btn interaction_btn">
                                <img class="icon" src="../../assets/svg/收藏.svg" alt="收藏">
                                <span>收藏</span>
                            </div>
                            <div class="love_btn interaction_btn">
                                <img class="icon" src="../../assets/svg/喜欢.svg" alt="喜欢">
                                <span>喜欢</span>
                            </div>
                        </div>
                        <div class="main_video_intruduction">
                            <div class="intruduction_item">
                                {{ intruduction_item }}
                                <div class="main_video_tags">
                                    <div class="tag_item" v-for="(item,index) in main_video_tags" :key="index">
                                        <span>{{item}}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <speaker_box/>
                <div class="send_comment_box">
                    <div class="send_user_avatar">
                        <img :src="'http://localhost:8000/static/img/thumbnail/'+user_info.avatar_path+'.png'">
                    </div>
                    <auto_textarea></auto_textarea>
                    <div class="send_btn">
                        <span>发送</span>
                    </div>
                </div>
                <comment_box></comment_box>
                <div class="the_end_page_box">
                    <the_end_page/>
                </div>
            </div>
            <div class="recommend_box">
                <recommend_box></recommend_box>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import recommend_box from './recommend_box.vue';
import speaker_box from './speaker_box.vue';
import the_end_page from './the_end_page.vue';
import auto_textarea from './auto_textarea.vue'
import comment_box from './comment_box.vue';


let user_info=ref(JSON.parse(localStorage.getItem('user')))
console.log(user_info.value)
let main_video_title=ref('气候变化的临界点——以及我们的现状')
let main_video_info=ref({
    watch_count:'10086',
    speaker:'Speaker Name',
    speaker_intruduction:'Speaker Intruduction',
    create_time:'2024-03-03'
})
let intruduction_item=ref(`我们已经快到 2020 年代的一半了，这个十年被称为应对气候变化最具决定性的十年。
现在的情况究竟如何？气候影响学者 Johan Rockström 对地球状况进行了最新的科学评估，
并解释了必须采取哪些措施来保持地球对人类压力的适应力。`)

let main_video_tags=ref(['标签1','标签2','标签3'])

// 主视频的播放路径
const video_path = ref('src/assets/video/v1.mp4')


// 更新主视频的剩余时间
function updateMainVideoTime(event) {
    const video = event.target
    console.log('主视频剩余时间:', Math.floor(video.duration - video.currentTime))
}


</script>

<style scoped>
.icon{
    width:25px;
    height: 25px;
    object-fit: cover;
}
.content_page {
    padding: 20px;
    overflow: hidden;
}

.content {
    width: 100%;
    height: auto;
    display: flex;
    gap: 10px;
}

.video_info {
    width: 70%;
    display: flex;
    flex-direction: column;
}

.video_box {
    width: 100%;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
}

.main-video {
    width: 100%;
    height: 400px;
}
.info_item{
    width: 100%;
    height: auto;
    max-height: 250px;
    display: flex;
    flex-direction: column;
    gap:10px;
}
.interaction_box{
    width:100%;
    height: auto;
    display: flex;
    gap:20px;
    border-top: 1px solid rgb(133,133,133);
    align-items: center;
    padding: 5px;
}
.interaction_btn{
    width: auto;
    display: flex;
    gap:5px;
    cursor: pointer;
    padding: 5px;
    border-radius: 5px;
}
.interaction_btn:hover{
    background-color: rgba(133,133,133,0.5);
    transform: scale(1.02);
    transform: translateY(-1px);
    
}
.main_video_intruduction{
    width:100%;
    display: flex;
    flex-direction: column;
    gap:10px;
}
.main_video_tags{
    display: flex;
    gap: 10px;
}
.tag_item{
    cursor: pointer;
    text-decoration-line: underline;
}
.recommend_box{
    max-height: 90vh;
    width:100%;
    margin-left: 20px;
}
.recommend_box::-webkit-scrollbar {
    display: none;
}
.send_comment_box{
    margin-top: 10px;
    width: auto;
    height: auto;
    display: flex;
    flex-direction: row;
    gap:8px;
    justify-content: center;
    align-items: center;
}
.send_user_avatar{
    width: 50px;
    height: 50px;
    min-height: 50px;
    min-width: 50px;
}
.send_user_avatar img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}
.send_btn{
    width: 80px;
    height: 100%;
    background-color: rgb(133,133,133);
    color: white;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}
.send_btn:hover{
    opacity: 0.8;
    transform: scale(1.02);
    transform: translateY(-1px);
}
</style>