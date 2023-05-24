<template>
  <div class="col-mb-6 movie-item">
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-img
          :src="imgSrc"
          alt="포스터 없음"
          v-bind="attrs"
          v-on="on"
        />
      </template>
      <MovieDetail :movie="movie" @close="dialog = false" />
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
