<template>
  <v-app>
    <!--Navbar-->
    <v-app-bar app color="light green darken 3" dark>
      <div class="d-flex align-center">
        <router-link to="/" id="title">Receptbank</router-link>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        :disabled="loading"
        to="/my-recipes"
        class="ma-1"
        color="white"
        plain
      >
        Recept
      </v-btn>
      <v-btn
        :disabled="loading"
        to="/inventory"
        class="ma-1"
        color="white"
        plain
      >
        Skafferi
      </v-btn>

      <v-btn :disabled="loading" to="/about" class="ma-1" color="white" plain>
        Om
      </v-btn>
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
