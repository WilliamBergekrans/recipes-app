<template>
  <v-container>
    <v-row>
      <RecipeCard class="ma-4" />
      <RecipeCard class="ma-4" />
      <RecipeCard class="ma-4" />
    </v-row>
    <v-row justify="center" class="mt-5">
      <v-btn class="mx-2">Slumpa recept</v-btn>
      <v-btn class="mx-2">Nytt recept</v-btn>
    </v-row>
  </v-container>
</template>

<script>
import RecipeCard from "../components/RecipeCard.vue";
import { mapGetters } from "vuex";

export default {
  name: "Home",
  data: () => ({
    recipes: {
      title: "",
      description: "",
      id: NULL,
    },
  }),
  components: {
    RecipeCard,
  },
  computed: { ...mapGetters(["getRandomRecipes"]) },
};
</script>
