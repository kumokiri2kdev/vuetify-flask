<template>
  <div>
    <v-card>
        <v-card-text>
          View A
        </v-card-text>
    </v-card>
    <v-list dense>
      <v-list-item
        v-for="(item, i) in items"
        :key="i"
      >
        <v-list-item-content>
          <v-list-item-title v-text="item"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'ViewA',
    data () {
      return {
        items:[],
        loading: true
      }
    },
    mounted () {
      axios
          .get('http://localhost:5000/geta',
              {headers: {'Access-Control-Allow-Origin': '*','Content-Type': 'application/json'}})
          .then(response => {
              console.log(response.data);
              this.items = response.data;
          })
          .catch(error => {
              console.log(error)
          })
          .finally(() => this.loading = false)
      },
  }
</script>
