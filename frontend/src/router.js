import Vue from 'vue'
import Router from 'vue-router'
import Layout from './views/Layout'

Vue.use(Router)

const routes = []


// 侧边栏菜单路由
routes.push(
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('./views/Login')
    },
    {
        path: '/Home',
        name: 'Home',
        component: Layout,
        children: [

            {
                path: '/Home',
                name: 'Home',
                meta: {
                    index: `/Home`,
                    title: '儀表盤',
                    type: 'menu',
                    active: false,
                    notCache: true
                },
                component: () => import('./views/DashBoard')
            },
             {
                path: 'asset/',
                name: 'asset',
                meta: {
                    title: '物理資源',
                    type: 'menu',
                    active: false,
                    notCache: true
                },
                component: () => import('./views/Asset')
            },
            {
                path: 'audit/',
                name: 'audit',
                meta: {
                    index: `/Home/audit`,
                    title: '登入歷史',
                    type: 'menu',
                    active: false,
                    notCache: true
                },
                component: () => import('./views/Audit')
            },
            {
                path: 'settings/',
                name: 'settings',
                meta: {
                    index: `/Home/settings`,
                    title: '頁面設定',
                    type: 'menu',
                    active: false,
                    notCache: true
                },
                component: () => import('./views/Setting')
            },
        ]
    },
    {
        name: '404',
        path: '/404',
        component: () => import('./views/notFound.vue')
    },
    {
        path: '*',    // 此处需特别注意至于最底部
        redirect: '/404'
    }
)



export default new Router({routes})
