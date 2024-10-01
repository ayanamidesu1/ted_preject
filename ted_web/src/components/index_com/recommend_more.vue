<template>
    <div class="recommend_more">
        <div class="content">
            <div class="item_list">
                <div class="item" v-for="(item, index) in recommend_video_list" :key="index">
                    <div class="video_box" @click="videoDetail(item.video_id)">
                        <video :src="'http://localhost:8000/static/video/'+item.video_file_path" ref="videoRefs" 
                        :muted="isMuted"
                        @loadedmetadata="setDuration(index)" 
                        @mouseenter="mouseEnter(index)" 
                        @mouseleave="mouseLeave(index)"></video>
                        <div class="video_time">
                            {{ item.duration }}
                        </div>
                        <div class="open_radio" @click="switch_sound($event)">
                            <img :src="'/src/assets/svg/'+(isMuted?'声音关.svg':'声音开.svg')" class="icon">
                        </div>
                    </div>
                    <div class="video_name">
                        <span>
                            {{ item.title }}
                        </span>
                    </div>
                    <div class="video_info">
                        <span style="color: rgb(133,133,133);font-size:12px;">{{ item.username }}
                            &nbsp;{{ item.watch_count }}次观看
                            &nbsp; {{ item.create_time }}</span>
                    </div>
                </div>
            </div>
            <div class="scroll_box">
                <scroll_box :msg_list="tags"></scroll_box>
            </div>
            <the_end_page></the_end_page>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import scroll_box from './scroll_box.vue'
import the_end_page from './the_end_page.vue';
import get_recommend_video from './js/get_recommend_video';

const store = useStore();
const router = useRouter();

let recommend_video_list = ref([])

//视频详情跳转
function videoDetail(id) {
    router.push('/content_page')
    store.commit('set_video_id',id)
}

//声音开关
let isMuted = ref(true)
function switch_sound(event) {
    //阻止默认冒泡事件
    event.stopPropagation()
    event.preventDefault();
    isMuted.value = !isMuted.value
}

let videoRefs = ref([]);

let tags=ref([])


// 通过 ref 获取视频元素并设置时长
function setDuration(index) {
    const videoElement = videoRefs.value[index];  // 通过 ref 引用视频
    if (videoElement) {
        const duration = videoElement.duration;
        const minutes = String(Math.floor(duration / 60)).padStart(2, '0');
        const seconds = String(Math.floor(duration % 60)).padStart(2, '0');
        recommend_video_list.value[index].duration = `${minutes}:${seconds}`;
    }
}

//鼠标在视频上的移入移出事件
function mouseEnter(index) {
    const videoElement = videoRefs.value[index];  // 通过 ref 引用视频
    if (videoElement) {
        videoElement.play();
    }
}

function mouseLeave(index) {
    const videoElement = videoRefs.value[index];  // 通过 ref 引用视频
    if (videoElement) {
        videoElement.pause();
    }
}

onMounted(async()=>{
    let temp_arr=await get_recommend_video()
    temp_arr=temp_arr.data
    let temp_arr2=[]
    let temp_tag_arr=[]
    for(let i=0;i<4;i++){
        temp_arr2.push(temp_arr[i])
        temp_arr2[i].duration='00:00:00'
        temp_tag_arr=temp_arr[i].tags.split(/[,，]/)
        for(let j=0;j<temp_tag_arr.length;j++){
            tags.value.push(temp_tag_arr[j])
        }
        temp_tag_arr=[]
    }
    recommend_video_list.value=temp_arr2
})

</script>

<style scoped>
.recommend_more {
    width: 100%;
    height: auto;
    min-height: 200px;
    display: flex;
    gap: 20px;
    margin-top: 10px;
    border-top: 1px solid rgb(133, 133, 133);
    margin-left: auto;
    margin-right: auto;
    padding-top: 20px;
    flex-direction: column;
}

.item_list {
    width: 90%;
    height: auto;
    min-height: 200px;
    display: flex;
    gap: 20px;
    margin: auto;
}

.item {
    width: calc(25% - 20px);
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.item video {
    width: 100%;
    height: 200px;
    object-fit: cover;
    cursor: pointer;
}

.video_box {
    position: relative;
}

.video_time {
    position: absolute;
    bottom: 5px;
    right: 5px;
    padding: 5px 10px;
    background-color: rgba(0, 0, 0, 0.3);
    color: white;
    border-radius: 5px;
}
.scroll_box{
    margin-top: 20px;
}
.open_radio{
    left: 5px;
    bottom: 5px;
    position: absolute;
    z-index: 2;
    cursor: pointer;
    padding: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    /*防止点击事件向下传播,仅在本事件传播*/
    pointer-events: stroke;
    z-index: 2;
}
.open_radio:hover{
    background-color: rgba(233,233,233,0.5);
    transition: all 0.2s ease-in-out;
    border-radius: 50%;
}
.icon{
    width: 25px;
    height: 25px;
    object-fit: cover;
}
</style>