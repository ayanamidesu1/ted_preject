<template>
    <div class="register_page">
        <div class="content">
            <div class="register_box">
                <h1>注册</h1>
                <div class="input_box">
                    <span>用户名：</span>
                    <input type="text" placeholder="请输入用户名" v-model="register_info.username" required>
                </div>
                <div class="input_box">
                    <span>选择头像：</span>
                    <div class="avatar_box">
                        <img class="avatar" :src="avatar" alt="头像">
                    </div>
                    <span @click="clickAvatarInput()" class="choose_btn">选择</span>
                    <input type="file" name="avatar" accept="image/*" @change="changeAvatar($event)" ref="avatarInput">
                    <div class="tips" style="margin-top: 10px;">
                        <span>仅支持JPG/JPEG、png、tiff格式图片，最大为10MB</span>
                    </div>
                </div>
                <div class="input_box">
                    <span>邮箱地址：</span>
                    <input type="email" placeholder="请输入邮箱地址" v-model="register_info.email" required>
                </div>
                <div class="input_box">
                    <span>密码：</span>
                    <input type="password" placeholder="请输入密码" v-model="register_info.password" required>
                </div>
                <div class="input_box">
                    <span>确认密码：</span>
                    <input type="password" placeholder="请再次输入密码" v-model="confirmPassword" required>
                </div>
                <div class="tips">
                    <span>密码长度最少8位，至少包含两种字符</span>
                </div>
                <div class="input_box" style="margin-top: 10px;">
                    <span>姓：</span>
                    <input type="text" placeholder="请输入姓" v-model="first_name" required>
                </div>
                <div class="input_box">
                    <span>名：</span>
                    <input type="text" placeholder="请输入名" v-model="last_name" required>
                </div>
                <div class="input_box">
                    <span>性别：</span>
                    <select v-model="sex" required>
                        <option value="男">男</option>
                        <option value="女">女</option>
                    </select>
                </div>
                <div class="input_box">
                    <span>生日：</span>
                    <input type="date" v-model="birthday" required>
                </div>
                <div class="error_msg" v-if="errorMessage">{{ errorMessage }}</div>
                <div class="register_btn">
                    <span @click="validateAndRegister">注册</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { register } from './register';
import { useRouter } from 'vue-router';

const router = useRouter()

let files = null
let register_info = ref({
    username: '',
    email: '',
    password: '',
    sex: '',
})
let first_name = ref('')
let last_name = ref('')
let sex = ref('')
let birthday = ref('')

let confirmPassword = ref('')
let avatar = ref('src/assets/svg/默认头像.svg')
let avatarInput = ref(null)
let errorMessage = ref('')
const store = useStore()

function clickAvatarInput() {
    avatarInput.value.click()
}

function changeAvatar(event) {
    const file = event.target.files[0]
    files = file
    if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
            avatar.value = e.target.result
        }
        reader.readAsDataURL(file)
    }
}

async function validateAndRegister() {
    errorMessage.value = ''
    if (register_info.value.password !== confirmPassword.value) {
        errorMessage.value = '两次输入的密码必须相同'
        return
    }

    if (!validatePassword(register_info.value.password)) {
        errorMessage.value = '密码必须大于8个字符，且包含至少两种不同类型的字符'
        return
    }

    let res =await register(files, register_info.value.username, register_info.value.password, first_name.value, last_name.value,
        register_info.value.email, sex.value, birthday.value
    )
    if (res.status == 200 || res.status == 201) {
        console.log(res)
        // 这里可以添加注册逻辑并处理头像文件
        router.push('/login')
    }
    else{   
        console.log(res)
    }

}

function validatePassword(password) {
    const hasUpperCase = /[A-Z]/.test(password)
    const hasLowerCase = /[a-z]/.test(password)
    const hasNumbers = /[0-9]/.test(password)
    const hasSpecialCharacters = /[!@#$%^&*(),.?":{}|<>]/.test(password)
    const isValidLength = password.length > 8
    return isValidLength && (hasUpperCase + hasLowerCase + hasNumbers + hasSpecialCharacters >= 2)
}
</script>

<style scoped>
.register_page {
    display: flex;
    justify-content: center;
    align-items: flex-start; /* 从顶部对齐，使得 margin 生效 */
    min-height: 100vh; /* 保证页面最小高度为视窗高度 */
    background-color: #f5f5f5;
    padding-top: 100px; /* 给顶部留 100px */
    padding-bottom: 100px; /* 给底部留 100px */
    box-sizing: border-box; /* 确保 padding 不影响宽度 */
}

.content {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    width: 500px;
    margin-top: auto;
    margin-bottom: auto;
    max-height: calc(100vh - 200px); /* 确保内容不会超出视窗 200px 的空隙 */
    box-sizing: border-box;
    overflow-y: auto; /* 当内容超出时允许滚动 */
}
.content::-webkit-scrollbar {
    width: none;
    height: none;
    display: none;
}

.register_box {
    display: flex;
    flex-direction: column;
}

.input_box {
    margin-bottom: 15px;
}

.avatar_box {
    margin-top: 10px;
    margin-bottom: 10px;
}

.avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    background-color: #f0f0f0;
}

.choose_btn {
    background-color: rgb(0, 150, 250);
    padding: 5px 10px;
    border-radius: 5px;
    color: white;
    cursor: pointer;
}

.choose_btn:hover {
    opacity: 0.8;
    transform: scale(1.01);
    transition: all 0.2s ease;
    transform: translateY(-1px);
}

input[type="text"],
input[type="password"],
input[type="email"] {
    width: 90%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin-top: 5px;
    transition: border-color 0.3s;
    margin: auto;
}

input[type="text"]:focus,
input[type="password"]:focus,
input[type="email"]:focus {
    border-color: #007bff;
}

input[type="file"] {
    display: none;
}

.error_msg {
    color: red;
    margin-bottom: 15px;
}

.register_btn span {
    display: inline-block;
    width: 90%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    text-align: center;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.register_btn span:hover {
    background-color: #0056b3;
}
</style>
