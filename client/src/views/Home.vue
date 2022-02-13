<template>
  <v-container>
    <v-row>
      <v-col> <RecipeCard /> </v-col>
    </v-row>
  </v-container>
</template>

<script>
import RecipeCard from "../components/RecipeCard.vue";

export default {
  name: "Home",
  components: {
    RecipeCard,
  },
};
</script>
