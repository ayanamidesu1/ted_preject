<template>
    <div class="index_recommend">
        <div class="content">
            <div class="video_info">
                <div class="recommend_title">
                    推荐理由
                </div>
                <div class="recommend_tag">
                    <span>推荐的内容标签</span>
                </div>
                <div class="recommend_video_title">
                    <span>推荐视频标题</span>
                </div>
                <div class="recommend_video_info">
                    <span>推荐视频简介</span>
                </div>
                <div class="recommend_video_d_info">
                    <span>推荐视频播放信息</span>
                    <div class="speaker_info">
                        <span>演讲人：{{ video_player_info.speaker }}</span>
                    </div>
                    <div class="video_play_info">
                        <span>{{ video_player_info.play_count }}次</span>.<span>大约 {{ time_since_creation }}</span>
                    </div>
                </div>
            </div>
            <div class="video_content">
                <div class="video_player">
                    <router-link to="/content_page">
                        <div class="jump_link">
                            <video class="video" :src="video_path" preload="auto" ref="videoElement"
                                @mouseenter="playVideo" @mouseleave="pauseVideo" @timeupdate="updateTime">
                            </video>
                            <div class="remaining_time">
                                剩余时间: {{ remainingTime }} 秒
                            </div>
                        </div>
                    </router-link>
                </div>
            </div>
        </div>
        <recommend_more></recommend_more>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import recommend_more from './recommend_more.vue';

// 使用 Vuex store 和 Vue Router
const store = useStore()
const router = useRouter()

// 视频信息
let video_player_info = ref({
    'play_count': 0,
    'create_time': '2024年9月20日18:45:15', // 创建时间
    'speaker': '张三' // 演讲人
})

// 视频路径
let video_path = ref('src/assets/video/Honkai  Star Rail 2024.03.03 - 12.20.34.03.mp4')

// 剩余时间
let remainingTime = ref(0)

// 引用视频元素
let videoElement = ref(null)

// 鼠标移入时播放视频
function playVideo() {
    videoElement.value.play()
}

// 鼠标移出时暂停视频
function pauseVideo() {
    videoElement.value.pause()
}

// 更新剩余时长
function updateTime() {
    if (videoElement.value) {
        remainingTime.value = Math.floor(videoElement.value.duration - videoElement.value.currentTime)
    }
}

// 计算时间差并选择合适的时间单位
function calculateTimeDifference(creationTime) {
    let now = new Date()
    let timeDiff = now.getTime() - new Date(creationTime).getTime() // 获取时间差（毫秒）

    let minutes = Math.floor(timeDiff / (1000 * 60)) // 转换为分钟
    if (minutes < 60) return `${minutes} 分钟前`

    let hours = Math.floor(minutes / 60) // 转换为小时
    if (hours < 24) return `${hours} 小时前`

    let days = Math.floor(hours / 24) // 转换为天
    if (days < 30) return `${days} 天前`

    let months = Math.floor(days / 30) // 转换为月
    if (months < 12) return `${months} 个月前`

    let years = Math.floor(months / 12) // 转换为年
    return `${years} 年前`
}

// 创建时间距今的时间显示
let time_since_creation = ref(calculateTimeDifference(video_player_info.value.create_time))

// Vuex 全局跳转示例，假设有一个跳转方法
function goToVideoPage(videoId) {
    // 使用 Vuex 管理跳转逻辑
    store.commit('SET_CURRENT_VIDEO', videoId)
    router.push({ name: 'VideoDetail', params: { id: videoId } })
}
</script>

<style scoped>
.index_recommend {
    width: 100%;
    height: auto;
    max-height: 35vh;
    display: flex;
    margin-top: 10px;
    flex-direction: column;
}

.content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    gap: 10px;
}

.video_content {
    width: 50%;
    height: auto;
    display: flex;
    margin-right: 10px;
}
.jump_link{
    position: relative;
}
.video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: relative;
}

.remaining_time {
    position: absolute;
    bottom: 5px;
    right: 10px;
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 3px 8px;
    font-size: 12px;
    border-radius: 3px;
    z-index: 2;
}

.video_info {
    width: calc(50% - 10px);
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-left: 40px;
    justify-content: center;
}

.recommend_title {
    font-weight: 600;
}

.recommend_tag {
    color: red;
}

.recommend_video_title {
    font-size: 28px;
    font-weight: 600;
}

.recommend_video_info {
    font-size: 14px;
}

.recommend_video_d_info {
    font-size: 14px;
}

.speaker_info {
    color: rgb(133, 133, 133);
}

.video_play_info {
    color: rgb(133, 133, 133);
}
</style>
