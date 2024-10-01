<template>
    <div class="content_page" :key="video_id">
        <div class="content" v-if="main_video_info">
            <div class="video_info">
                <div class="video_box">
                    <!-- 主视频播放器 -->
                    <video class="main-video" controls :src="video_path" @timeupdate="updateMainVideoTime"></video>
                    <div class="info_item">
                        <div class="main_video_tite">
                            {{main_video_info.title}}
                        </div>
                        <div class="main_video_data">
                            <span>{{main_video_info.watch_count}}次观看</span>|
                            <span>{{main_video_info.username}}</span>|
                            <span>{{main_video_info.introduce}}</span>|
                            <span>{{main_video_info.create_time}}</span>
                        </div>
                        <div class="interaction_box">
                            <div class="share_btn interaction_btn">
                                <img class="icon" src="../../assets/svg/分享.svg" alt="分享">
                                <span>分享</span>
                            </div>
                            <div class="collect_btn interaction_btn" @click="interaction_video_a(video_id,'collect')">
                                <img class="icon" 
                                :src="'http://localhost:8000/static/svg/'+(main_video_info.is_collect?'收藏.svg':'没收藏.svg')" alt="收藏">
                                <span>收藏</span>
                                <span>{{main_video_info.collect_count}}</span>
                            </div>
                            <div class="love_btn interaction_btn" @click="interaction_video_a(video_id,'like')">
                                <img class="icon" 
                                :src="'http://localhost:8000/static/svg/'+(main_video_info.is_like?'喜欢.svg':'不喜欢.svg')" alt="喜欢">
                                <span>喜欢</span>
                                <span>{{main_video_info.like_count}}</span>
                            </div>
                        </div>
                        <div class="main_video_intruduction">
                            <div class="intruduction_item">
                                {{ main_video_info.video_introduce }}
                                <div class="main_video_tags">
                                    <div class="tag_item" v-for="(item,index) in main_video_info.tags" :key="index">
                                        <span>{{item}}</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <speaker_box :user_info="main_video_info"/>
                <div class="send_comment_box">
                    <div class="send_user_avatar">
                        <img :src="'http://localhost:8000/static/img/thumbnail/'+user_info.avatar_path+'.png'">
                    </div>
                    <comment_input_box :video_id="video_id" :comment_type="'comment'" />
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
import { ref, onMounted,computed } from 'vue'
import recommend_box from './recommend_box.vue';
import speaker_box from './speaker_box.vue';
import the_end_page from './the_end_page.vue';
import auto_textarea from './auto_textarea.vue'
import comment_box from './comment_box.vue';
import comment_input_box from './comment_input_box.vue';
import { useStore } from 'vuex';
import get_video_info from './js/get_video_info';
import interaction_video from './js/interaction_video';

const store = useStore()

let video_id=computed(()=>store.getters.video_id)
console.log(video_id.value)

let user_info=ref(JSON.parse(localStorage.getItem('user')))
console.log(user_info.value)
let main_video_info=ref({})

// 主视频的播放路径
const video_path = ref('src/assets/video/v1.mp4')

// 更新主视频的剩余时间
function updateMainVideoTime(event) {
    const video = event.target
    console.log('主视频剩余时间:', Math.floor(video.duration - video.currentTime))
}

//视频交互
async function interaction_video_a(video_id,interaction_type){
    try {
        let res=await interaction_video(video_id,interaction_type)
        if(res.status==200){
            if(interaction_type=='like'){
                main_video_info.value.is_like=!main_video_info.value.is_like
                if(main_video_info.value.is_like){
                    main_video_info.value.like_count+=1
                }
                else{
                    main_video_info.value.like_count-=1
                }
            }
            else if(interaction_type=='collect'){
                main_video_info.value.is_collect=!main_video_info.value.is_collect
                if(main_video_info.value.is_collect){
                    main_video_info.value.collect_count+=1
                }
                else{
                    main_video_info.value.collect_count-=1
                }
            }
            console.log(res)
        }
        else{
            console.log(res)
        }
    }
    catch (error) {
        console.log(error)
    }
}

onMounted(async function(){
    let res=await get_video_info(video_id.value)
    res=res.data
    res.tags=res.tags.split(/[,，]/)
    main_video_info.value=res
    console.log(res)
})

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