<template>
  <div>
    <v-card>
        <v-card-text>
          {{content}}
        </v-card-text>
    </v-card>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'ViewCDetail',
    data () {
      return {
        content: ''
      }
    },
    mounted () {
      axios
          .get('http://localhost:5000/getbd/' + this.$route.params.key,
              {headers: {'Access-Control-Allow-Origin': '*','Content-Type': 'application/json'}})
          .then(response => {
              console.log(response.data);
              this.content = response.data;
          })
          .catch(error => {
              console.log(error)
          })
          .finally(() => this.loading = false)
    },
    methods: {

    }
  }
</script>
