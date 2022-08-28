<template>
  <div>
    <v-card>
        <v-card-text>
          {{content}}
        </v-card-text>
        <v-textarea
          name="input"
          label="メモ"
          v-model="memo"
          hint="メモを入力"
        ></v-textarea>
        <v-btn depressed
        @click="send_memo()">
          送信
        </v-btn>
    </v-card>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'ViewDMemo',
    data () {
      return {
        content: '',
        memo: ''
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
     axios
          .get('http://localhost:5000/getmemo/' + this.$route.params.key,
              {headers: {'Access-Control-Allow-Origin': '*','Content-Type': 'application/json'}})
          .then(response => {
              console.log(response.data);
              this.memo = response.data;
          })
          .catch(error => {
              console.log(error)
          })
          .finally(() => this.loading = false)

    },
    methods: {
      send_memo:function() {
        console.log(this.memo)
        axios.post('http://localhost:5000/memo',
          {
            memo: this.memo,
            key: this.$route.params.key
          },
          {
            headers: {
              'Access-Control-Allow-Origin': '*',
              'Content-Type': 'application/json'
            }
          })
          .then(response => {
            console.log(response.data);
            this.content = response.data;
          })
          .catch(error => {
            console.log(error)
          })
          .finally(() => this.loading = false)
      }
    }
  }
</script>
