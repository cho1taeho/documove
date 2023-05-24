<template>
  <div class="giving-theme">
    <div class="container">
      <div class="row">
        <div class="col-4" v-for="giving in givings" :key="giving.id">
          <div class="card">
            <img :src="giving.imageLink" class="card-img-top" :alt="giving.title">
            <div class="card-body">
              <h5 class="card-title">{{ giving.title }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import {  useRoute } from 'vue-router'
// const route = useRoute()
// const theme_id = route.query.theme_id

export default {
  data() {
    return {
      givings: [],
    };
  },
  async created() {
    // const theme_id = this.$route.params.theme_id || 'your_default_theme_id';
      const theme_id = this.$route.query.theme_id
      console.log(theme_id)
    // const route = useRoute()
    // const theme_id = route.query.theme_id
    if (theme_id) {
      const response = await axios.get(`http://127.0.0.1:8000/movies/giving/`);
      console.log(response)
      this.givings = response.data.filter(movie => movie.themes.theme[0].id === theme_id);
      console.log(this.givings)
    }
  }
};
</script>

<style scoped>
.card {
  margin-bottom: 20px;
}
</style>