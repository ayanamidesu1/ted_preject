<template>
  <div class="scroll_box">
    <div class="scroll_box_content">
      <div class="btn_box">
        <div class="left_btn" @click="scrollLeft">
          <img :src="props.left_btn" class="icon">
        </div>
        <div class="right_btn" @click="scrollRight">
          <img :src="props.right_btn" class="icon">
        </div>
      </div>
      <div class="list" ref="list">
        <div class="item" v-for="(item, index) in props.msg_list" :key="index">
          <span>{{item}}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, defineProps, defineEmits } from 'vue';
import { useStore } from 'vuex';
const store = useStore();

const props = defineProps({
  left_btn: {
    type: String,
    default: 'src/assets/svg/left.svg'
  },
  right_btn: {
    type: String,
    default: 'src/assets/svg/right.svg'
  },
  msg_type: {
    type: String,
    default: 'image'
  },
  msg_list: {
    type: Array,
    default: () => []
  },
  animationDuration: {
    type: Number,
    default: 500 // Default animation duration in ms
  },
  scrollDistance: {
    type: Number,
    default: 400 // Default scroll distance in px
  }
});

const colorArr = ref([
  'rgb(126, 183, 200)', 'rgb(126, 186, 200)', 'rgb(157, 200, 126)', 'rgb(200, 126, 170)', 'rgb(200, 126, 146)',
  'rgb(126, 129, 200)', 'rgb(167, 126, 200)', 'rgb(200, 170, 126)', 'rgb(126, 200, 167)', 'rgb(126, 200, 129)'
]);

const tags_item = ref(null);
const list = ref(null);

const set_tag_color = () => {
  if (tags_item.value) {
    tags_item.value.forEach((item, index) => {
      item.style.backgroundColor = colorArr.value[index % colorArr.value.length];
    });
  }
};

const emit = defineEmits(['chose_item']);
const chose_item = (item) => {
  emit('chose_item', item);
};

// Easing function for smooth animation
const easeInOutQuad = (t) => {
  return t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t;
};

const smoothScroll = (distance, duration) => {
  const start = list.value.scrollLeft;
  const startTime = performance.now();

  const animateScroll = (currentTime) => {
    const elapsedTime = currentTime - startTime;
    const progress = Math.min(elapsedTime / duration, 1);
    const ease = easeInOutQuad(progress);

    list.value.scrollLeft = start + distance * ease;

    if (progress < 1) {
      requestAnimationFrame(animateScroll);
    }
  };

  requestAnimationFrame(animateScroll);
};

const scrollLeft = () => {
  smoothScroll(-props.scrollDistance, props.animationDuration);
};

const scrollRight = () => {
  smoothScroll(props.scrollDistance, props.animationDuration);
};

//用户详情页跳转
function jump_to_other_user_center(userid,item)
{
  store.commit('SET_OTHER_USERID',userid)
  store.commit('SET_SINGLE_PAGE_STATUS',{'key':'other_user_center_page','value':true})
  console.log(userid)
}

onMounted(() => {
  set_tag_color();
  console.log(props)
});
</script>

<style scoped>
.scroll_box {
  width: 100%;
  height: 100%;
  min-height: 30px;
  min-width: 50px;
  display: flex;
  align-items: center;
  max-height: 300px;
  position: relative; /* 将 position 移到父容器以控制 btn_box 的位置 */
}
/*禁用横向滚动条显示*/
.scroll_box::-webkit-scrollbar {
  display: none;
}

.scroll_box_content {
  display: flex;
  width: 100%;
  height: 100%;
  align-items: center;
  white-space: nowrap;
  overflow: hidden;
}

.btn_box {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  position: absolute;
  top: 0;
  opacity: 0;
  transition: opacity 0.2s ease-in-out;
  z-index: 5;
  pointer-events: none;
}

.scroll_box:hover .btn_box {
  opacity: 1;
}

.left_btn,
.right_btn {
  width: 60px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: absolute;
  pointer-events: auto;
}

.left_btn {
  left: 0;
  background: linear-gradient(to right, rgba(255, 255, 255, 1), rgba(255, 255, 255, 0));
}

.right_btn {
  right: 0;
  background: linear-gradient(to left, rgba(255, 255, 255, 1), rgba(255, 255, 255, 0));
}

.icon {
  width: 25px;
  height: 25px;
}

.list {
  display: flex;
  gap: 10px;
  white-space: nowrap;
  overflow-x: auto;
  scrollbar-width: none;
}
.left::-webkit-scrollbar{
  height: 0px;
  display: none;
  width: 0px;
}

.item {
  display: flex;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
  background-color: rgba(133,133,133,1);
  transition: all 0.2s;
}
.item:hover {
  opacity: 0.8;
  transform: scale(1.05);
  transform: translateX(-1px);
}


</style>
