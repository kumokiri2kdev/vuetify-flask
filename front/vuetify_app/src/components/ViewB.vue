<template>
  <div>
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          詳細
        </v-card-title>

        <v-card-text>
          {{content}}
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
            >
            閉じる
            </v-btn>
          </v-card-actions>
      </v-card>
    </v-dialog>
    <v-card>
        <v-card-text>
          View B
        </v-card-text>
    </v-card>
    <v-list dense>
      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        @click="link_clicked(item.key)"
      >
        <v-list-item-content>
          <v-list-item-title v-text="item.title"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'ViewB',
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
      },
      link_clicked:function(key) {
        console.log(key);

        axios
            .get('http://localhost:5000/getbd/' + key,
                {headers: {'Access-Control-Allow-Origin': '*','Content-Type': 'application/json'}})
            .then(response => {
                console.log(response.data);
                this.set_content(response.data);
            })
            .catch(error => {
                console.log(error)
            })
            .finally(() => this.loading = false)

      }
    }
  }
</script>
