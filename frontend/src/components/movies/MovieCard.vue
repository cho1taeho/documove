<template>
  <div class="col-mb-6 movie-item">
    <v-img
      v-if="movie.poster_path"
      :src="imgSrc"
      alt="포스터 없음"
      class="movie-poster"
      @click="goToMovieDetail(movie.id)"
    />
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
  computed: {
    imgSrc: function () {
      return this.movie.poster_path ? "https://image.tmdb.org/t/p/original" + this.movie.poster_path : ''
    },
  },
  methods: {
    goToMovieDetail(movieId) {
      console.log(this.movie)
      console.log(movieId)
      this.$router.push({name:'MovieDetail', query: {movieId : movieId} })
    }

  },
  async created() {
    const movieId = this.$route.query.movieId;
    if (movieId) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/movie/`);
        this.movie = response.data.filter(movie => movie.id === movieId);
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>

<style scoped>
.movie-poster {
  width: 100%;
  position: relative;
  overflow: hidden;
}

.movie-item {
  margin-bottom: 20px;
}
</style>

