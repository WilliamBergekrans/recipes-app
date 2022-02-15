<template>
  <v-row class="justify-center">
    <RecipeCard
      v-for="recipe in recipes"
      :key="recipe.name"
      :name="recipe.name"
      :description="recipe.description"
      class="ma-4"
    />
  </v-row>
</template>

<script>
import RecipeCard from "../components/RecipeCard.vue";
import axios from "axios";

export default {
  name: "RecipeCards",
  data: () => ({
    recipes: [],
  }),
  components: {
    RecipeCard,
  },
  props: {
    loggedIn: { type: Boolean, default: false },
  },
  methods: {
    async getRecipes() {
      // Get the access token from the auth wrapper
      const token = await this.$auth.getTokenSilently();

      // Use Axios to make a call to the API
      const { data } = await axios.get("http://localhost:5000/get-recipes", {
        headers: {
          Authorization: `Bearer ${token}`, // send the access token through the 'Authorization' header
        },
      });

      this.recipes = data.recipes;
    },
    async getRecipesGeneral() {
      // Use Axios to make a call to the API
      const { data } = await axios.get(
        "http://localhost:5000/get-recipes-general"
      );

      this.recipes = data.recipes;
    },
  },
  created() {
    if (this.loggedIn == true) {
      this.getRecipes();
    } else {
      this.getRecipesGeneral();
    }
  },
};
</script>
