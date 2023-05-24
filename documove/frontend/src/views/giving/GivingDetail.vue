<template>
  <div class="giving-detail">
    <div class="container">
      <div class="row">
        <div class="col">
          <h1>{{ giving.title }}</h1>
          <p>{{ giving.summary }}</p>
          <!-- 나머지 필드들을 원하는 대로 표시하세요 -->
          <p>Theme: {{ giving.themeName }}</p>
          <p>Country: {{ giving.country }}</p>
          <p>Region: {{ giving.region }}</p>
          <p>Funding: {{ giving.funding }}</p>
          <p>Remaining: {{ giving.remaining }}</p>
          <!-- 필요한 필드들을 추가하세요 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data() {
    return {
      giving: null,
    };
  },
  async created() {
    const giving_id = this.$route.query.id
    if (giving_id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/movies/giving`)
        this.givings = response.data.id
      } catch(error) {
        console.error(error)
      }
    }    
  },
};
</script>

<style scoped>

</style>
