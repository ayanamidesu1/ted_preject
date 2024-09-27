<template>
    <div class="comment_input_box">
        <!-- 将 v-model 绑定到 auto_textarea 上 -->
        <auto_textarea v-model="text" />
        <div class="send_btn" @click="sendComment">
            <span>发送</span>
        </div>
    </div>
</template>

<script setup>
import { ref, defineProps, defineEmits, watch } from 'vue';
import auto_textarea from './auto_textarea.vue';

// 定义 props 和 emits
let props = defineProps({
    modelValue: {
        type: String,
        default: ''
    }
});

let emit = defineEmits(['update:modelValue']);

// 内部的 text 值
let text = ref(props.modelValue);

// 监听 text 变化，发射事件更新父组件的 modelValue
watch(text, (newValue) => {
    emit('update:modelValue', newValue);
});

// 监听 props.modelValue 的变化同步到内部的 text
watch(
    () => props.modelValue,
    (newValue) => {
        text.value = newValue;
    }
);

// 发送评论功能（根据实际逻辑实现）
function sendComment() {
    if (text.value.trim()) {
        console.log('发送评论:', text.value);
        // 发送完评论后清空输入框
        text.value = '';
    }
}
</script>

<style scoped>
.comment_input_box {
    width: 100%;
    height: 100%;
    display: flex;
    gap: 10px;
}

.send_btn {
    width: auto;
    height: auto;
    padding: 5px 10px;
    display: flex;
    cursor: pointer;
    background-color: rgba(133, 133, 133, 0.8);
    transition: all 0.2s;
    border-radius: 10px;
    width: 50px;
    align-items: center;
    justify-content: center;
}

.send_btn:hover {
    opacity: 0.6;
    transform: scale(1.02);
    transform: translateY(-1px);
}
</style>