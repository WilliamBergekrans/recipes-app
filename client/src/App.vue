<template>
  <v-app>
    <v-app-bar app color="lime" dark>
      <div class="d-flex align-center">
        <h1>Min receptbank</h1>
      </div>

      <v-spacer></v-spacer>
      <router-link to="/about"> Om </router-link>
      <v-icon>mdi-open-in-new</v-icon>
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
