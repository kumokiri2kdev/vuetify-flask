<template>
  <v-list-item>
    <v-list-item-content>
      <v-list-item-title v-text="key_val"></v-list-item-title>
      <v-list-item-subtitle v-text="title"></v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
  export default {
    name: 'ViewFChild',
    props: ['key_val', 'title']
  }
</script>
