# フロントエンド
## アプリ作成

```
$ vue create app
```
```
Vue CLI v5.0.6
┌─────────────────────────────────────────┐
│                                         │
│   New version available 5.0.6 → 5.0.8   │
│    Run npm i -g @vue/cli to update!     │
│                                         │
└─────────────────────────────────────────┘

? Please pick a preset:
  Default ([Vue 3] babel, eslint)
❯ Default ([Vue 2] babel, eslint)
  Manually select features
```

### アプリ起動
```
$ cd app
$ npm run serve
```
成功すると下記のようになる。
```
DONE  Compiled successfully in 3536ms                                                                         11:11:39


 App running at:
 - Local:   http://localhost:8080/
 - Network: http://10.0.1.4:8080/

 Note that the development build is not optimized.
 To create a production build, run yarn build.
```



## Vuetify の追加

app フォルダ以下で実行。

```
$ vue add vuetify
```
```
? Choose a preset: (Use arrow keys)
  Vuetify 2 - Configure Vue CLI (advanced)
❯ Vuetify 2 - Vue CLI (recommended)
  Vuetify 2 - Prototype (rapid development)
  Vuetify 3 - Vite (preview)
  Vuetify 3 - Vue CLI (preview)
```
## Router の追加

```
npm install vue-router@3
```
@3 がないとエラーとなる。

app/src 下に router.js を追加。
```
$ touch router.js
```

main.js ルーターのモジュール を追加
``` javascript:main.js
import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router' // ここ

Vue.config.productionTip = false

new Vue({
  vuetify,
  router: router,  //ここ
  render: h => h(App)
}).$mount('#app')
```
App.vue の v-main を変更。
```
<v-main>
  <router-view />
</v-main>
```
HelloWorld のコンポーネントは削除。

## 最初のページ

components 下に TopPage.vue を追加。

```
<template>
  <div>
    <v-card>
      <v-responsive :aspect-ratio="16/9">
        <v-card-text>
          This card will always be 16:9 (unless you put more stuff in it)
        </v-card-text>
      </v-responsive>
    </v-card>
  </div>
</template>

<script>
  export default {
    name: 'TopPage',
  }
</script>
```
router.js を変更。

```
import Vue from 'vue'
import Router from 'vue-router'
import TopPage from './components/TopPage.vue'

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
  ]
})
```
## ルートの追加

## axios の追加
### vuetify 側
app フォルダ以下で実行。
```
$ npm install axios --save
```













# サーバー
