import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    randomRecipes: [{}],
  },
  mutations: {},
  actions: {},
  getters: {
    getRandomRecipes: (state) => {
      return state.randomRecipes;
    },
  },
});
