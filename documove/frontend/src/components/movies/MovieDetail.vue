<template>
  <div class="movie-detail-card">
    <div class="movie-detail-toolbar">
      <v-btn
        icon
        dark
        @click="$emit('close')"
      >
        <v-icon>mdi-close</v-icon>
      </v-btn>
      <img id="logo-image" src="@/assets/images/logo.png" />
    </div>
    <div class="movie-detail-body">
      <div class="movie-detail-poster">
        <img :src="movie.poster_path" alt="포스터 없음" />
      </div>
      <div class="movie-detail-info">
        <div class="movie-detail-title">{{ movie.title }}</div>
        <div v-if="movie.release_date" class="movie-release-date">
          개봉: {{ movie.release_date }}
        </div>
        <div v-if="movie.overview" class="movie-overview">
          줄거리: {{ movie.overview }}
        </div>
        <div class="movie-original-title">
          원제: {{ movie.original_title }}
        </div>
        <div class="movie-original-language">
          원래 언어: {{ movie.original_language }}
        </div>
        <div class="movie-popularity">
          인기도: {{ movie.popularity }}
        </div>
        <div class="movie-vote-count">
          투표 수: {{ movie.vote_count }}
        </div>
        <div class="movie-vote-average">
          평점: {{ movie.vote_average }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDetail',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
.movie-detail-card {
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.movie-detail-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.movie-detail-poster {
  margin-right: 20px;
}

.movie-detail-info {
  font-size: 14px;
  line-height: 1.4;
  margin-bottom: 20px;
}

.movie-detail-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.movie-release-date,
.movie-overview,
.movie-original-title,
.movie-original-language,
.movie-popularity,
.movie-vote-count,
.movie-vote-average {
  margin-bottom: 5px;
}
</style>
