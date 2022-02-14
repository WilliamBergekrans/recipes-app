<template>
  <v-app>
    <!--Navbar-->
    <v-app-bar app color="light green darken 3" dark>
      <div class="d-flex align-center">
        <router-link to="/" id="title">Receptbank</router-link>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        v-if="$auth.isAuthenticated"
        to="/my-recipes"
        class="ma-1"
        color="white"
        plain
      >
        Recept
      </v-btn>
      <v-btn
        v-if="$auth.isAuthenticated"
        to="/inventory"
        class="ma-1"
        color="white"
        plain
      >
        Skafferi
      </v-btn>

      <v-btn to="/about" class="ma-1" color="white" plain> Om </v-btn>

      <div v-if="!$auth.loading">
        <!-- show login when not authenticated -->
        <v-btn v-if="!$auth.isAuthenticated" @click="login" plain color="white"
          >Logga in</v-btn
        >
        <!-- show logout when authenticated -->
        <v-btn v-if="$auth.isAuthenticated" @click="logout" plain color="white"
          >Logga ut</v-btn
        >
      </div>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    },
    // Log the user out
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin,
      });
    },
  },
};
</script>

<style scoped>
#title {
  font-family: "Courier New", Courier, monospace;
  font-size: 30px;
  text-decoration: none;
  color: white;
}
</style>
