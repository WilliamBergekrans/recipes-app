<template>
  <v-container>
    <RecipeCards v-if="$auth.isAuthenticated" :loggedIn="true" />
    <RecipeCards v-else-if="!$auth.isAuthenticated && !$auth.loading" />
    <v-row justify="center" class="mt-5">
      <v-btn class="mx-2">Slumpa recept</v-btn>
      <v-btn class="mx-2">Nytt recept</v-btn>
    </v-row>
  </v-container>
</template>

<script>
import RecipeCards from "../components/RecipeCards.vue";

export default {
  name: "Home",
  components: {
    RecipeCards,
  },
};
</script>
