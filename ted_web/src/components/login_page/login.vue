<template>
    <div class="login_page">
        <div class="content">
            <!-- 账号输入框 -->
            <div class="login_box_account" :class="{ 'slide-in-right': !emailEntered, 'slide-out-left': emailEntered }"
                v-if="!emailEntered">
                <div class="tips">
                    <span>输入你的账号</span>
                </div>
                <span>用户名</span>
                <div class="input_box">
                    <input type="text" v-model="username" placeholder="请输入用户名">
                </div>
                <div class="continue" @click="continueToPassword">
                    <span>继续</span>
                </div>
            </div>

            <!-- 密码输入框 -->
            <div class="login_box_password" :class="{ 'slide-in-left': emailEntered, 'slide-out-right': !emailEntered }"
                v-if="emailEntered">
                <div class="tips">
                    <span>输入你的密码</span>
                </div>
                <span>密码</span>
                <div class="input_box">
                    <input type="password" v-model="password" placeholder="请输入密码">
                </div>
                <div class="login_btn" @click="login">
                    <span>登录</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import {get_token} from '../auto_token_auth'

const router = useRouter();
const store = useStore();

// 邮箱和状态
const username = ref('')
const password=ref('')
const emailEntered = ref(false)

// 点击继续时触发
function continueToPassword() {
    if (validateEmail(username.value)) {
        emailEntered.value = true
    } else {
        alert('请输入有效的邮箱地址')
    }
}

// 简单的邮箱验证函数
function validateEmail(email) {
    //const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return  true//re.test(email)
}

// 登录按钮点击事件（接口待定）
async function login() {
    console.log(username.value)
    console.log(password.value)
    let res=await get_token(username.value,password.value)
    if(res.status==200){
    store.commit('SET_SINGLE_PAGE_STATUS',{'key':'index_page_show','value':true})
    //alert('登录接口待定')
    let auth_token=res.access
    let refresh_token=res.refresh
    localStorage.setItem('auth_token',auth_token)
    localStorage.setItem('refresh_token',refresh_token)
    router.push('/')
    }
    else{
        alert('用户名或密码错误')
        console.log(res)
    }
}
</script>

<style scoped>
/* 页面布局 */
.login_page {
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.content {
    width: 300px;
    position: relative;
}

/* 输入框容器 */
.login_box_account,
.login_box_password {
    position: absolute;
    width: 100%;
    height: auto;
    padding: 20px;
    background-color: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    transition: all 0.3s ease-in-out;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.tips {
    margin-bottom: 10px;
}

.input_box input {
    width: 90%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    outline: none;
    margin: auto;
}

.continue,
.login_btn {
    width: 90%;
    text-align: center;
    padding: 10px;
    background-color: #1E90FF;
    color: white;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.continue:hover,
.login_btn:hover {
    background-color: #1C86EE;
}

/* 动画效果 */
/* 从右侧进入 */
.slide-in-right {
    transform: translateX(100%);
    animation: slideInFromRight 0.3s forwards;
}

@keyframes slideInFromRight {
    0% {
        transform: translateX(100%);
    }

    100% {
        transform: translateX(0);
    }
}

/* 从左侧消失 */
.slide-out-left {
    transform: translateX(0);
    animation: slideOutToLeft 0.3s forwards;
}

@keyframes slideOutToLeft {
    0% {
        transform: translateX(0);
    }

    100% {
        transform: translateX(-100%);
    }
}

/* 从左侧进入 */
.slide-in-left {
    transform: translateX(-100%);
    animation: slideInFromLeft 0.3s forwards;
}

@keyframes slideInFromLeft {
    0% {
        transform: translateX(-100%);
    }

    100% {
        transform: translateX(0);
    }
}

/* 从右侧消失 */
.slide-out-right {
    transform: translateX(0);
    animation: slideOutToRight 0.3s forwards;
}

@keyframes slideOutToRight {
    0% {
        transform: translateX(0);
    }

    100% {
        transform: translateX(100%);
    }
}
</style>