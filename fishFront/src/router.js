// history模式
import {createRouter, createWebHashHistory,} from 'vue-router'

import Recommend from './pages/Recommend/Recommend.vue'
import Home from './pages/Home/Home.vue'
import Register from "@/pages/Register/Register.vue";
import Merchants from "@/pages/Merchants/Merchants.vue";
import Administrator from "@/pages/Administrator/Administrator.vue";
import PersonalInfo from "@/pages/PersonalInfo/PersonalInfo.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        // component: Administrator,
        component: Home,
    },

    {
        path: '/Register',
        name: 'Register',
        component: Register,
    },
    {
        path: '/PersonalInfo',
        name: 'PersonalInfo',
        component: PersonalInfo,
    },
    {
        path: '/Recommend',
        name: 'Recommend',
        component: Recommend,
    },
    {
        path: '/Merchants',

        
        name: 'Merchants',
        component: Merchants,
    },
    {
        path: '/Administrator',
        name: 'Administrator',
        component: Administrator,
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})
export default router;
