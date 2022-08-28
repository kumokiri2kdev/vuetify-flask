import Vue from 'vue'
import Router from 'vue-router'
import TopPage from './components/TopPage.vue'
import ViewA from './components/ViewA.vue'
import ViewB from './components/ViewB.vue'
import ViewC from './components/ViewC.vue'
import ViewCDetail from './components/ViewC_Detail.vue'
import ViewD from './components/ViewD.vue'
import ViewDMemo from './components/ViewDMemo.vue'
import ViewE from './components/ViewE.vue'

Vue.use(Router)

export default new Router({
  // デフォルトの挙動では URL に `#` が含まれる.
  // URL から hash を取り除くには `mode:history` を指定する
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'TopPage',
      component: TopPage
    },
    {
      path: '/view_a',
      name: 'ViewA',
      component: ViewA
    },
    {
      path: '/view_b',
      name: 'ViewB',
      component: ViewB
    },
    {
      path: '/view_c',
      name: 'ViewC',
      component: ViewC
    },
    {
      path: '/view_c_detail/:key',
      name: 'ViewCDetail',
      component: ViewCDetail
    },
    {
      path: '/view_d',
      name: 'ViewD',
      component: ViewD
    },
    {
      path: '/view_d_memo',
      name: 'ViewDMemo',
      component: ViewDMemo
    },
    {
      path: '/view_e',
      name: 'ViewE',
      component: ViewE
    },
  ]
})
