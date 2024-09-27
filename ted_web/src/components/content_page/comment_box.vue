<template>
  <div class="comment_box">
    <h2>评论</h2>
    <div class="content">
      <!-- 遍历主评论和子评论 -->
      <div class="comment_group" v-for="(mainComment, index) in displayedMainComments" :key="mainComment.id">
        <!-- 主评论 -->
        <div class="main_comment">
          <div class="comment_info">
            <div class="user_box">
              <div class="avatar">
                <img :src="'http://localhost:8000/static/img/thumbnail/' + mainComment.avatar_path + '.png'" alt="用户头像">
              </div>
            </div>
            <div class="comment_content">
              <div class="username">
                <span>{{ mainComment.author }}</span>
              </div>
              <p>{{ mainComment.comment_content }}</p>
              <div class="comment_interaction">
                <div class="interaction_box">
                  <div class="inter_box">
                    <img src="../../assets/svg/点赞.svg" alt="点赞">
                    <span></span>
                  </div>
                  <div class="inter_box">
                    <img src="../../assets/svg/踩.svg" alt="踩">
                    <span></span>
                  </div>
                  <div class="inter_box" @click="toggleReplyInput(index, 0)">
                    <img src="../../assets/svg/留言.svg" alt="回复">
                    <span>回复</span>
                  </div>
                </div>
                <span>{{ mainComment.send_time }}</span>
              </div>

              <!-- 主评论回复框 -->
              <comment_input_box v-if="comment_input_box_show[index][0]" />
            </div>
          </div>
        </div>

        <!-- 子评论 -->
        <div class="reply_comments" v-for="(reply, replyIndex) in displayedSubComments(index)" :key="reply.comment_id">
          <div class="reply_comment">
            <div class="comment_info">
              <div class="user_box">
                <div class="avatar">
                  <img :src="'http://localhost:8000/static/img/thumbnail/' + reply.avatar_path + '.png'" alt="用户头像">
                </div>
              </div>
              <div class="comment_content">
                <div class="username">
                  <span>{{ reply.author }}</span>
                </div>
                <p>回复: {{ reply.comment_content }}</p>
                <div class="comment_interaction">
                  <div class="interaction_box">
                    <div class="inter_box">
                      <img src="../../assets/svg/点赞.svg" alt="点赞">
                      <span></span>
                    </div>
                    <div class="inter_box">
                      <img src="../../assets/svg/踩.svg" alt="踩">
                      <span></span>
                    </div>
                    <div class="inter_box" @click="toggleReplyInput(index, replyIndex + 1)">
                      <img src="../../assets/svg/留言.svg" alt="回复">
                      <span>回复</span>
                    </div>
                  </div>
                  <span>{{ reply.send_time }}</span>
                </div>
                <!-- 子评论回复框 -->
                <comment_input_box v-if="comment_input_box_show[index][replyIndex + 1]" />
              </div>
            </div>
          </div>
        </div>

        <!-- 子评论查看更多按钮 -->
        <div class="show_more_sub"
          v-if="sub_comment_list[index] && sub_comment_list[index].length > sub_display_limit[index]">
          <span @click="loadMoreSubComments(index)">查看更多子评论</span>
        </div>
      </div>

      <!-- 主评论查看更多按钮 -->
      <div class="show_more" v-if="main_total > main_display_limit">
        <span @click="loadMoreMainComments">查看更多</span>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, computed } from 'vue';
import { get_comment_list, get_reply_comment_list } from './js/get_comment';
import { useStore } from 'vuex';
import comment_input_box from './comment_input_box.vue';

const store = useStore();

let main_comment_list = ref([]); // 主评论列表
let main_total = ref(0); // 主评论总数
let main_display_limit = ref(1); // 每次显示的主评论数量

let sub_comment_list = ref([]); // 存储每个主评论对应的子评论
let sub_total = ref([]); // 每个主评论的子评论总数
let sub_display_limit = ref([]); // 每个主评论的子评论显示数量

let video_id = computed(() => store.getters.video_id); // 视频 ID

let main_limit = ref(5); // 主评论加载数量
let main_offset = ref(0); // 主评论偏移量
let sub_limit = ref(10000); // 子评论加载数量

// 初始化回复框显示状态的二维数组
let comment_input_box_show = ref([]);

// 获取主评论
async function getMainCommentList() {
  let res = await get_comment_list(video_id.value, main_limit.value, main_offset.value);
  if (res.status == 200) {
    res = res.data;
    main_comment_list.value.push(...res.rows);
    main_total.value = res.total;
    main_offset.value += main_limit.value;

    // 初始化每个主评论对应的子评论和显示限制
    res.rows.forEach((comment, index) => {
      sub_comment_list.value[index] = [];
      sub_display_limit.value[index] = 1; // 默认显示1条子评论
      comment_input_box_show.value[index] = [false]; // 主评论的回复框默认不显示
    });
  } else {
    console.warn('获取主评论失败');
  }
}

// 获取子评论
async function getSubCommentList(mainCommentId, index) {
  let res = await get_reply_comment_list(video_id.value, mainCommentId, sub_limit.value);
  if (res.status == 200) {
    res = res.data;
    sub_comment_list.value[index].push(...res.rows);

    // 初始化每个子评论的回复框显示状态
    for (let i = 0; i < res.rows.length; i++) {
      comment_input_box_show.value[index].push(false); // 子评论的回复框默认不显示
    }
  } else {
    console.warn('获取子评论失败');
  }
}

// 切换回复框显示状态
function toggleReplyInput(mainIndex, subIndex) {
  // 如果点击的是主评论，则只影响主评论的回复框显示状态
  comment_input_box_show.value[mainIndex].forEach((_, i) => {
    comment_input_box_show.value[mainIndex][i] = i === subIndex ? !comment_input_box_show.value[mainIndex][i] : false;
  });
}

// 查看更多主评论
function loadMoreMainComments() {
  main_display_limit.value += 3; // 每次显示3条主评论
  getMainCommentList();
}

// 查看更多子评论
function loadMoreSubComments(index) {
  sub_display_limit.value[index] += 3; // 每次显示3条子评论
}

// 计算当前显示的主评论
const displayedMainComments = computed(() => {
  return main_comment_list.value.slice(0, main_display_limit.value);
});

// 计算当前显示的子评论
function displayedSubComments(index) {
  if (sub_comment_list.value[index]) {
    return sub_comment_list.value[index].slice(0, sub_display_limit.value[index]);
  }
  return [];
}

// 初始化评论加载
onMounted(async () => {
  await getMainCommentList();
  for (let i = 0; i < main_comment_list.value.length; i++) {
    await getSubCommentList(main_comment_list.value[i].comment_id, i);
  }
});
</script>


<style scoped>
.comment_box {
  width: 100%;
  margin: 20px 0;
}

h2 {
  margin-bottom: 10px;
}

.content {
  width: 100%;
}

.comment_group {
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.comment_info {
  display: flex;
  align-items: flex-start;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 8px;
}

.user_box {
  display: flex;
  align-items: center;
  margin-right: 10px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.username {
  margin-left: 10px;
  font-weight: bold;
}

.comment_content {
  flex: 1;
}

.comment_interaction {
  font-size: 12px;
  color: #888;
  margin-top: 5px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.interaction_box {
  width: auto;
  display: flex;
  gap: 10px;
  align-items: center;
  justify-content: center;
}

.inter_box {
  display: flex;
  cursor: pointer;
  padding: 5px;
}

.inter_box:hover {
  border-radius: 50%;
  background-color: rgba(133, 133, 133, 1);
}

.inter_box img {
  width: 20px;
  height: 20px;
  object-fit: cover;
}

.reply_comment {
  margin-left: 40px;
}

.show_more {
  text-align: center;
  margin-top: 20px;
  cursor: pointer;
}

.show_more:hover {
  text-decoration: underline;
}

.show_more span {
  color: #007bff;
  width: 80px;
}

.show_more_sub {
  cursor: pointer;
  width: 150px;
}

.show_more_sub:hover {
  text-decoration: underline;
}
</style>
