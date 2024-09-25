<template>
  <div class="the_end_page">
    <div class="content">
        <h1>THE END</h1>
        <div class="tag_list">
            <div class="tag_item">
                <h3>探索</h3>
                <div class="tag_item_content">
                    <div class="item">
                        <span>项目一</span>
                    </div>
                    <div class="item">
                        <span>项目二</span>
                    </div>
                    <div class="item">
                        <span>项目三</span>
                    </div>
                    <div class="item">
                        <span>项目四</span>
                    </div>
                </div>
            </div>
            <div class="tag_item">
                <h3>我们的社区</h3>
                <div class="tag_item_content">
                    <div class="item">
                        <span>项目一</span>
                    </div>
                    <div class="item">
                        <span>项目二</span>
                    </div>
                    <div class="item">
                        <span>项目三</span>
                    </div>
                    <div class="item">
                        <span>项目四</span>
                    </div>
                </div>
            </div>
            <div class="tag_item">
                <h3>时事通讯</h3>
                <div class="tag_item_content">
                    <div class="tips_box">
                        <img src="../../assets/svg/邮箱.svg" class="icon">
                        <span>获取最新会谈</span>
                    </div>
                    <span style="font-size: 12px;">每天收到一封包含最新谈话热门内容的快速组合的电子邮件。</span>
                    <div class="input_box">
                        <input type="text" placeholder="你的电子邮箱是什么？" v-model="email">
                        <div class="btn">
                            <span>订阅</span>
                        </div>
                    </div>
                    <span>
                        通过订阅，您理解并同意我们将根据我们的隐私政策存储、处理和管理您的个人信息
                    </span>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

let email = ref('')
</script>

<style scoped>
.the_end_page{
    width:100vw;
    height: auto;
    padding-top:20px;
    padding-left: 10px;
    padding-right: 10px;
    padding-bottom: 20px;
    background-color: black;
    color: white;
    margin-top: 20px;
    margin-left: -20px;
    z-index: 2;
    margin-bottom: -20px;
}
.tag_list{
    width: 80%;
    height: auto;
    display: flex;
    justify-content: space-between;
}
.tag_item{
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: column;
    gap:10px;
}
.tag_item_content{
    display: flex;
    gap:5px;
    flex-direction: column;
}
.item{
    cursor: pointer;
    width: 80px;
}
.item:hover{
    text-decoration: underline;
}
.icon{
    width: 25px;
    height: 25px;
    object-fit: cover;
}
.tips_box{
    display: flex;
    gap: 15px;
    align-items: center;
}
.input_box{
    width: 100%;
    height: 40px;
    display: flex;
    background-color: white;
    border:1px solid rgb(133,133,133);
    border-radius: 5px;
}
.input_box input{
    width:80%;
    height: 100%;
    outline: none;
    border:none;
    background: none;
}
.btn{
    width: 20%;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    color: white;
    background-color: black;
    border-radius: 2px;
    margin: 1px;
}
</style>