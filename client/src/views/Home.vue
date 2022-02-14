<template>
  <v-container>
    <v-row>
      <RecipeCard
        name="Spagetti Bolognese"
        description="En pasta med krämig köttfärsås"
        class="ma-4"
      />
      <RecipeCard
        name="Vegetasik lasagne"
        description="Pasta i flera lager med grönsaker och keso"
        class="ma-4"
      />
      <RecipeCard
        name="Pannkakor"
        description="MMMMM ägg, mjölk och sylt etc"
        class="ma-4"
      />
    </v-row>
    <v-row justify="center" class="mt-5">
      <v-btn class="mx-2">Slumpa recept</v-btn>
      <v-btn class="mx-2">Nytt recept</v-btn>
      <v-btn @click="getRecipes">Recepttest</v-btn>
    </v-row>
  </v-container>
</template>

<script>
import RecipeCard from "../components/RecipeCard.vue";
import { mapGetters } from "vuex";
import axios from "axios";

export default {
  name: "Home",
  data: () => ({
    recipes: [],
  }),
  components: {
    RecipeCard,
  },
  computed: { ...mapGetters(["getRandomRecipes"]) },
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

      this.recipes = data;
    },
  },
};
</script>
