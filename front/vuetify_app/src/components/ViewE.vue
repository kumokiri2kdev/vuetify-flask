<template>
  <div>
    <v-card>
        <v-card-text>
          View E
        </v-card-text>
    </v-card>
    <div>
      <div class="ma-auto" style="max-width: 500px">
        <v-text-field
          v-model="input_text"
          label="Main input">
        </v-text-field>
        <v-subheader class="pl-0 mb-8">
          Always show thumb label
        </v-subheader>
        <v-slider
          v-model="slider"
          thumb-label="always"
        ></v-slider>
        <v-select
          v-model=seleced_item
          :items="items"
          label="Outlined style"
          outlined
        ></v-select>
      </div>
      <div class="ma-auto text-right" style="max-width: 500px">
        <v-btn depressed
          @click="send_form()">
          送信
        </v-btn>
      </div>
    </div>
  </div>
</template>


<script>
  import axios from 'axios'
  export default {
    name: 'ViewE',
    data () {
      return {
        slider: 0,
        input_text: '',
        seleced_item :'やらない',
        items : ['やる', 'やらない', 'わからない']
      }
    },
    methods: {
      send_form:function() {
        console.log(this.slider)
        console.log(this.input_text)
        console.log(this.seleced_item)
        axios.post('http://localhost:5000/form',
          {
            text: this.input_text,
            val: this.slider,
            selected: this.seleced_item
          },
          {
            headers: {
              'Access-Control-Allow-Origin': '*',
              'Content-Type': 'application/json'
            }
          })
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
