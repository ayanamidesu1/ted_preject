import { createStore } from 'vuex';
import { RootState } from './store.d'; // 引入RootState类型

// 最大栈深度
const MAX_STACK_DEPTH = 500;

const store = createStore<RootState>({
    state: {
        pageStatus: {
            login_page_show: false,
            index_page_show:true,
            register_page_show: false,
        },
        content_page: {},
        pageStack: [],
        pushTimer: null,
        video_id: '',
    },
    mutations: {
        SET_SINGLE_PAGE_STATUS(state:any, { key = '', value = false }) {
            if (key === 'all') {
                for (const k in state.pageStatus) {
                    if (Object.prototype.hasOwnProperty.call(state.pageStatus, k) && typeof state.pageStatus[k] === 'boolean') {
                        state.pageStatus[k] = false;
                    }
                }
                return;
            }
            for (const k in state.pageStatus) {
                if (Object.prototype.hasOwnProperty.call(state.pageStatus, k) && typeof state.pageStatus[k] === 'boolean') {
                    state.pageStatus[k] = false;
                }
            }
            state.pageStatus[key] = value;
            const allFalse = Object.keys(state.pageStatus).every(k => typeof state.pageStatus[k] !== 'boolean' || state.pageStatus[k] === false);
            if (allFalse) {
                state.pageStatus.index_page = true;
            }
        },
        SET_CONTENT_PAGE(state:any, { key = '', value = false }) {
            for (const k in state.content_page) {
                if (Object.prototype.hasOwnProperty.call(state.content_page, k) && typeof state.content_page[k] === 'boolean') {
                    state.content_page[k] = false;
                }
            }
            state.content_page[key] = value;
        },
        PUSH_PAGE_STATE(state:any) {
            if (state.pageStack.length >= MAX_STACK_DEPTH) {
                state.pageStack.shift(); // 删除最早的记录
            }
            state.pageStack.push({
                pageStatus: JSON.parse(JSON.stringify(state.pageStatus)), // 深拷贝页面状态
                content_page: JSON.parse(JSON.stringify(state.content_page)), // 深拷贝内容页面状态
            });
        },
        POP_PAGE_STATE(state:any) {
            if (state.pageStack.length > 0) {
                const previousState = state.pageStack.pop();
                state.pageStatus = previousState.pageStatus;
                state.content_page = previousState.content_page;
            }
        },
        RESET_PAGE_STACK(state:any) {
            state.pageStack = [];
            state.pushTimer = null; // 清除定时器
        },
        set_video_id(state:any, video_id:any) {
            state.video_id = video_id;
        }
    },
    actions: {
        goBack({ commit }:{commit:Function}) {
            commit('POP_PAGE_STATE'); // 恢复上一个状态
        }
    },
    getters: {
        login_page_show: (state:any) => state.pageStatus.login_page_show,
        index_page_show: (state:any) => state.pageStatus.index_page_show,
        register_page_show: (state:any) => state.pageStatus.register_page_show,
        video_id: (state:any) => state.video_id
    },
});

export default store;
