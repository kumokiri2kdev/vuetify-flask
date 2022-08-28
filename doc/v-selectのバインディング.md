## ラベルと値を同じにする場合

```javascript
<template>
  <div>
    <v-select
      v-model=seleced_item
      :items="items"
      label="Outlined style"
      outlined
    ></v-select>
  </div>
</template>
<script>
  export default {
    name: 'ViewE',
    data () {
      return {
        seleced_item :'やらない',
        items : ['やる', 'やらない', 'わからない']
      }
    },
  }
</script>

```


## ラベルと値を別々にする場合

[VuetifyでSelectタグを使う時の注意点](https://takumon.com/vuetify-select-tag)
