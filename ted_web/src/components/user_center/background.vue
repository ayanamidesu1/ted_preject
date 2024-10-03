<template>
    <div class="background">
        <div class="content">
            <div class="background_img">
                <img :src="'http://localhost:8000/static/img/img/102718099_p0.jpg'" alt="背景">
            </div>
            <div class="user_box">
                <div class="avatar">
                    <img :src="'http://localhost:8000/static/img/thumbnail/' + data.avatar_path + '.png'"
                        ref="avatar_file_img">
                    <div class="edit_avatar" @click="select_avatar">
                        <img src="http://localhost:8000/static/svg/图像.svg" alt="编辑头像">
                        <span>编辑头像</span>
                        <input type="file" ref="edit_file" style="display:none;" @change="set_file($event)">
                    </div>
                </div>
                <div class="user_info">
                    <div class="username" @mouseenter="showEditIcon('username')" @mouseleave="hideEditIcon('username')">
                        <div contenteditable="false" ref="username_text">
                            <span></span>
                        </div>
                        <div class="edit_info_box" :class="{ show_icon: username_edit_icon }"
                            @click="enableEdit('username')">
                            <img src="http://localhost:8000/static/svg/编辑.svg" alt="编辑" class="icon">
                        </div>
                    </div>
                    <div class="user_tags" @mouseenter="showEditIcon('tags')" @mouseleave="hideEditIcon('tags')">
                        <div contenteditable="false" ref="user_tags_text">
                            <span></span>
                        </div>
                        <div class="edit_info_box" :class="{ show_icon: tags_edit_icon }" @click="enableEdit('tags')">
                            <img src="http://localhost:8000/static/svg/编辑.svg" alt="编辑" class="icon">
                        </div>
                    </div>
                </div>
                <div class="self_website">
                    <div class="website" @mouseenter="showEditIcon('website')" @mouseleave="hideEditIcon('website')">
                        <div contenteditable="false" ref="website_text">
                            <span>{{ data.self_website }}</span>
                        </div>
                        <div class="edit_info_box" :class="{ show_icon: website_edit_icon }"
                            @click="enableEdit('website')">
                            <img src="http://localhost:8000/static/svg/编辑.svg" alt="编辑" class="icon">
                        </div>
                    </div>
                    <div class="self_website_introduce" @mouseenter="showEditIcon('introduce')"
                        @mouseleave="hideEditIcon('introduce')">
                        <div contenteditable="false" ref="website_introduce_text">
                            <span>{{ data.self_website_introduce }}</span>
                        </div>
                        <div class="edit_info_box" :class="{ show_icon: introduce_edit_icon }"
                            @click="enableEdit('introduce')">
                            <img src="http://localhost:8000/static/svg/编辑.svg" alt="编辑" class="icon">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="float_msg_box" :class="message_box_show?'float_msg_box_show':'float_msg_box_hidden'">
            <img src='http://localhost:8000/static/svg/完成.svg' alt="完成" style="width:25px;height:25px;object-fit:cover;">
            <span>{{message}}</span>
        </div>
    </div>
</template>

<script setup>
import { ref, defineProps, computed, onMounted, nextTick, onUnmounted } from 'vue'
import { edit_user_avatar,edit_user_info } from './js/edit_user_info';

let edit_file = ref(null)
let username_text = ref(null)
let user_tags_text = ref(null)
let website_text = ref(null)
let website_introduce_text = ref(null)

//弹窗消息
let message = ref('失败')
let message_box_show = ref(false)

let username_edit_icon = ref(false)
let tags_edit_icon = ref(false)
let website_edit_icon = ref(false)
let introduce_edit_icon = ref(false)

//文件变量
let file = new File([], '')
let avatar_file_img = ref(null)
let files

//设置文件
async function set_file(event) {
    const file = event.target.files[0];
    if (file) {
        //使用FileReader加载文件避免开发服务器依赖
        const reader = new FileReader();
        reader.onload = (e) => {
            avatar_file_img.value.src = e.target.result; // 使用 FileReader 加载文件
        };
        reader.readAsDataURL(file);
    }
    let res=await edit_user_avatar(file)
    if(res.status==200){
        message.value='修改成功'
        message_box_show.value=true
        nextTick(()=>{
            setTimeout(()=>{
                message_box_show.value=false
            },2000)
        })
    }else{
        message.value='修改失败'
        message_box_show.value=true
        nextTick(()=>{
            setTimeout(()=>{
                message_box_show.value=false
            },1000)
        })
    }
}

let props = defineProps({
    user_info: Object
})
let data = computed(() => props.user_info.data.user_info)

// 选择头像模拟点击
function select_avatar() {
    edit_file.value.click()
}

// 监控输入更新值
function username_change() {
    data.value.username = username_text.value.innerText
}
function user_tags_change() {
    data.value.user_tags = user_tags_text.value.innerText
}
function website_change() {
    data.value.self_website = website_text.value.innerText
}
function website_introduce_change() {
    data.value.self_website_introduce = website_introduce_text.value.innerText
}

// 显示编辑图标
function showEditIcon(type) {
    if (type === 'username') username_edit_icon.value = true
    else if (type === 'tags') tags_edit_icon.value = true
    else if (type === 'website') website_edit_icon.value = true
    else if (type === 'introduce') introduce_edit_icon.value = true
}

// 隐藏编辑图标
function hideEditIcon(type) {
    if (type === 'username') username_edit_icon.value = false
    else if (type === 'tags') tags_edit_icon.value = false
    else if (type === 'website') website_edit_icon.value = false
    else if (type === 'introduce') introduce_edit_icon.value = false
}

// 启用编辑模式
function enableEdit(type) {
    if (type === 'username') {
        username_text.value.contentEditable = 'true'
        username_text.value.focus()
        setCursorToEnd(username_text.value)
    } else if (type === 'tags') {
        user_tags_text.value.contentEditable = 'true'
        user_tags_text.value.focus()
        setCursorToEnd(user_tags_text.value)
    } else if (type === 'website') {
        website_text.value.contentEditable = 'true'
        website_text.value.focus()
        setCursorToEnd(website_text.value)
    } else if (type === 'introduce') {
        website_introduce_text.value.contentEditable = 'true'
        website_introduce_text.value.focus()
        setCursorToEnd(website_introduce_text.value)
    }
}

// 设置光标到文本的最后
function setCursorToEnd(element) {
    let range = document.createRange()
    let selection = window.getSelection()
    range.selectNodeContents(element)
    range.collapse(false)
    selection.removeAllRanges()
    selection.addRange(range)
}

// 提交修改接口（预留）
async function submitChanges(type) {
    if (type === 'username') {
        // 这里调用接口，提交用户名修改
        console.log('提交用户名:', data.value.username)
        let res=await edit_user_info('username',username=data.value.username,)
        if(res.status==200){
            message.value=res.msg
        }
    } else if (type === 'tags') {
        // 这里调用接口，提交用户标签修改
        console.log('提交用户标签:', data.value.user_tags)
        let res=await edit_user_info('user_tags',null,data.value.user_tags,null,null)
        if(res.status==200){
            message.value=res.msg
        }
    } else if (type === 'website') {
        // 这里调用接口，提交个人网站修改
        console.log('提交个人网站:', data.value.self_website)
        let res=await edit_user_info('self_website',null,null,data.value.self_website)
        if(res.status==200){
            message.value=res.msg
        }
    } else if (type === 'introduce') {
        // 这里调用接口，提交个人网站介绍修改
        console.log('提交网站介绍:', data.value.self_website_introduce)
        let res=await edit_user_info('self_website_introduce',null,null,null,data.value.self_website_introduce)
        if(res.status==200){
            message.value=res.msg
        }
    }
    showMessage()
}

//通知弹窗
function showMessage() {
    message_box_show.value = true
    setTimeout(() => {
        message_box_show.value = false
    }, 1000)
}

// 设置初始值
onMounted(async () => {
    await nextTick()
    if (username_text.value) {
        username_text.value.innerText = data.value.username
        user_tags_text.value.innerText = data.value.user_tags
        website_text.value.innerText = data.value.self_website
        website_introduce_text.value.innerText = data.value.self_website_introduce
    }
    username_text.value.addEventListener('input', username_change)
    user_tags_text.value.addEventListener('input', user_tags_change)
    website_text.value.addEventListener('input', website_change)
    website_introduce_text.value.addEventListener('input', website_introduce_change)

    await nextTick()
    if (username_text.value) {
        username_text.value.addEventListener('blur', () => submitChanges('username'))
        user_tags_text.value.addEventListener('blur', () => submitChanges('tags'))
        website_text.value.addEventListener('blur', () => submitChanges('website'))
        website_introduce_text.value.addEventListener('blur', () => submitChanges('introduce'))
    }
})

onUnmounted(() => {
    username_text.value.removeEventListener('input', username_change)
    user_tags_text.value.removeEventListener('input', user_tags_change)
    website_text.value.removeEventListener('input', website_change)
    website_introduce_text.value.removeEventListener('input', website_introduce_change)

    username_text.value.removeEventListener('blur', () => submitChanges('username'))
    user_tags_text.value.removeEventListener('blur', () => submitChanges('tags'))
    website_text.value.removeEventListener('blur', () => submitChanges('website'))
    website_introduce_text.value.removeEventListener('blur', () => submitChanges('introduce'))
})
</script>

<style scoped>
.icon {
    width: 25px;
    height: 25px;
    object-fit: cover;
    transition: transform 0.2s ease-in-out;
}

.content {
    width: 100%;
    height: 100%;
    display: flex;
    position: relative;
}

.background_img {
    width: 100%;
    height: 25%;
    display: flex;
}

.background_img img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.user_box {
    width: auto;
    height: 100px;
    display: flex;
    position: absolute;
    left: 10px;
    bottom: 10px;
    gap: 10px;
    background-color: rgba(255, 255, 255, 0.7);
    padding: 10px 20px;
    border-radius: 15px;
}

.avatar {
    width: 100px;
    height: 100px;
    display: flex;
    position: relative;
    overflow: hidden;
    border-radius: 50%;
}

.avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
}

.edit_avatar {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
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

.edit_avatar:hover {
    opacity: 1;
    transform: scale(1.05);
    transform: translateY(-1px);
}

.edit_avatar img {
    width: 30px;
    height: 30px;
    object-fit: cover;
    border-radius: 0;
}

.user_info {
    display: flex;
    flex-direction: column;
    gap: 5px;
    justify-content: space-around;
    max-width: 200px;
    overflow: hidden;
}

.username,
.user_tags,
.website,
.self_website_introduce {
    display: flex;
    gap: 5px;
    width: auto;
}

.edit_info_box {
    display: none;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.show_icon {
    display: flex;
}

.edit_info_box:hover .icon {
    transform: translateY(-1px) scale(1.02);
}

.self_website {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}
.float_msg_box{
    width:auto;
    position: fixed;
    top:200px;
    left: 50%;
    transition: 0.8s ease-in-out;
    opacity: 0;
    transform: translateY(50px);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
    padding: 5px 10px;
    background: rgba(255, 255, 255, 0.7);
    border-radius: 5px;
}
.float_msg_box_show{
    opacity: 1;
    transform: translateY(0px);
}
.float_msg_box_hidden{
    opacity: 0;
    transform: translateY(50px);
}
</style>