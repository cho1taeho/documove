<template>
  <div class="col-mb-6 movie-item">
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <template v-slot:activator="{ on, attrs }">
        <router-link :to="{ name: 'MovieDetail', params: { movieId: movie.id }}">
          <v-img
            :src="imgSrc"
            alt="포스터 없음"
            v-bind="attrs"
            v-on="on"
          />
        </router-link>
      </template>
      <MovieDetail :movieId="movie.id" @close="dialog = false" />
    </v-dialog>
  </div>
</template>


<script>
import MovieDetail from '@/components/movies/MovieDetail'

export default {
  name: 'MovieCard',
  components: {
    MovieDetail
  },
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
  data() {
    return {
      dialog: false,
    }
  },
  computed: {
    imgSrc: function () {
      return "https://image.tmdb.org/t/p/original" + this.movie.poster_path
    },
  },
}
</script>

<style scoped>
/* 필요한 CSS 스타일을 여기에 추가하세요 */
</style>
