<template>
  <div class="giving-theme">
    <div class="container">
      <div class="row">
        <div class="col-4" v-for="giving in givings" :key="giving.id">
          <div class="card" @click="goToGivingDetail(giving.id)">
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


export default {
  data() {
    return {
      givings: [],
    };
  },
  methods: {
    goToGivingDetail(giving_id) {
      
      this.$router.push({name:'GivingDetail', query: {giving_id : giving_id}})
    },
  },
  async created() {
    const theme_id = this.$route.query.theme_id;
    if (theme_id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/movies/giving/`);
        this.givings = response.data.filter(movie => movie.themes.theme[0].id === theme_id);
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
.card {
  margin-bottom: 20px;
}
</style>