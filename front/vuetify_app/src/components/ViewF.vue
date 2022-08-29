<template>
  <div>
    <v-card>
        <v-card-text>
          View F
        </v-card-text>
    </v-card>
    <v-list dense>
      <ViewFChild
        v-for="(item, i) in items"
        :key="i"
        @click="link_clicked(item.key)"
        :key_val=item.key
        :title=item.title
      >
      </ViewFChild>
    </v-list>
  </div>
</template>

<script>
  import axios from 'axios'
  import ViewFChild from './ViewFChild.vue'
  export default {
    name: 'ViewF',
    components: {ViewFChild},
    data () {
      return {
        items:[],
        dialog: false,
        content: '',
        loading: true
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
      set_content: function(content) {
        this.content = content;
        this.dialog = true;
      }
    }
  }
</script>
