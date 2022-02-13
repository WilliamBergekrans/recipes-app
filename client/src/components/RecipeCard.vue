<template>
  <v-card class="mx-auto" max-width="344">
    <v-img :src="image" height="200px"></v-img>

    <v-card-title> {{ name }} </v-card-title>

    <v-card-subtitle> {{ description }} </v-card-subtitle>

    <v-card-actions>
      <v-btn color="orange lighten-2" text to="/about"> Gå till recept </v-btn>

      <v-spacer></v-spacer>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "RecipeCard",
  props: {
    name: { type: String, required: true },
    description: { type: String, required: true },
    id: { type: Number, required: false },
    image: {
      type: String,
      default: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    },
  },
};
</script>
