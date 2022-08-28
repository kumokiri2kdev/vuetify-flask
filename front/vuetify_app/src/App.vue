<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
      fixed
    >
      <v-container class="d-flex align-center">
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
      </v-container>
    </v-app-bar>
    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
    <v-footer
      color="primary lighten-1"
      padless
    >
      <v-row
        justify="center"
        no-gutters
      >
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
        >
          <router-link to="/">Top</router-link>
        </v-btn>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
        >
          <router-link to="/view_a">View A</router-link>
        </v-btn>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
        >
          <router-link to="/view_b">View B</router-link>
        </v-btn>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
        >
          <router-link to="/view_c">View C</router-link>
        </v-btn>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
        >
          <router-link to="/view_d">View D</router-link>
        </v-btn>
        <v-btn
          color="white"
          text
          rounded
          class="my-2"
        >
          <router-link to="/view_e">View E</router-link>
        </v-btn>
      </v-row>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    //
  }),
};
</script>
