<template>
  <div>
    <v-card>
        <v-card-text>
          View C
        </v-card-text>
    </v-card>
    <v-list dense>
      <v-list-item
        v-for="(item, i) in items"
        :key="i"
      >
        <v-list-item-content>
          <router-link :to="{name:'ViewCDetail',params:{key:item.key}}">{{item.title}}</router-link>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'ViewC',
    data () {
      return {
        items:[],
        dialog: false,
        content: ''
      }
    },
    mounted () {
      axios
          .get('http://localhost:5000/getb',
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
    methods: {
      link_clicked:function(key) {
        console.log(key);

        axios
            .get('http://localhost:5000/getbd/' + key,
                {headers: {'Access-Control-Allow-Origin': '*','Content-Type': 'application/json'}})
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error)
            })
            .finally(() => this.loading = false)

      }
    }
  }
</script>
