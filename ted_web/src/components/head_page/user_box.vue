<template>
    <div class="user_box" v-if="userinfo">
        <div class="content">
            <div class="user_info">
                <div class="avatar" @click="toggleDropdown">
                    <img :src="'http://localhost:8000/static/img/thumbnail/' + userinfo.avatar_path + '.png'" alt="头像">
                </div>
                <div class="info_dropdown_box" :class="{ 'info_dropdown_box_show': dropdown_show, 'info_dropdown_box_hide': !dropdown_show }">
                    <span>用户名</span>
                    <div class="info_item">
                        <span>{{ userinfo.username }}</span>
                    </div>
                    <span>邮箱</span>
                    <div class="info_item">
                        <span>{{ userinfo.email }}</span>
                    </div>
                    <div class="info_item">
                        <span>进入个人中心</span>
                    </div>
                    <div class="info_item">
                        <span @click="clear">退出登录</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted,onUnmounted } from 'vue';
import { get_userinfo } from './get_userinfo';
import { useRouter } from 'vue-router';

const router = useRouter();
let userinfo = ref(JSON.parse(localStorage.getItem('user')));
let dropdown_show = ref(false);

// 切换下拉框显示
const toggleDropdown = () => {
    dropdown_show.value = !dropdown_show.value;
};

// 清空 localStorage 和 cookie
const clear = () => {
    localStorage.clear();
    document.cookie = '';
    location.reload();
    router.push('/login');
};


onMounted(async () => {
    let res = await get_userinfo();
    if (res.status == 200) {
        localStorage.setItem('user', JSON.stringify(res.data));
        console.log(res);
    }
    //点击非用户信息区域，隐藏下拉框
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.user_info')) {
            dropdown_show.value = false;
        }
    });
});
onUnmounted(() => {
    document.removeEventListener('click', (e) => {
        if (!e.target.closest('.user_info')) {
            dropdown_show.value = false;
        }
    });
})
</script>

<style scoped>
.user_box {
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: column;
}

.content {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.user_info {
    width: 100%;
    height: auto;
    display: flex;
    background-color: rgba(255, 255, 255, 1);
    position: relative;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.avatar {
    width: 50px;
    height: 50px;
    display: flex;
    cursor: pointer; /* 鼠标悬停样式 */
}

.avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}

.info_dropdown_box {
    width: auto;
    height: auto;
    display: flex;
    flex-direction: column;
    position: absolute;
    top: calc(100% + 15px);
    max-width: 150px;
    overflow: hidden;
    background-color: rgba(255, 255, 255, 1);
    gap: 10px;
    padding: 5px;
    border-radius: 5px;
    transition: opacity 0.3s ease, transform 0.3s ease;
    opacity: 0; /* 初始透明度为0 */
    transform: translateY(-10px); /* 初始向上偏移 */
}

.info_dropdown_box_show {
    opacity: 1; /* 显示时透明度为1 */
    transform: translateY(0); /* 恢复到原位 */
}

.info_dropdown_box_hide {
    opacity: 0; /* 隐藏时透明度为0 */
    transform: translateY(-10px); /* 隐藏时向上偏移 */
}

.info_item {
    padding: 8px; /* 内边距 */
    cursor: pointer; /* 鼠标样式 */
    transition: background 0.3s; /* 背景色过渡效果 */
}

.info_item:hover {
    background-color: #f0f0f0; /* 悬停时背景颜色 */
}
</style>
