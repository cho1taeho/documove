<template> 
  <div class="movie-detail-card">
    <div class="movie-detail-toolbar">
      <v-btn
        icon
        dark
        @click="$router.go(-1)"
      >
        <v-icon>mdi-close</v-icon>
      </v-btn>
      <img id="logo-image" src="@/assets/images/logo.png" />
    </div>
    <div class="movie-detail-body">
       <div class="movie-detail-poster">
        <img :src="imgSrc" alt="포스터 왜 없음" />
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
        <div class="movie-review">
        <!-- <input type="text"/> -->
        <button @click="addPoint()">포인트적립하기</button>
        <!-- <button @click="">point</button> -->
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
      movie: [],
    }
  },
  components:{

  },
  methods: {
    async addPoint() {
      const movieId = this.$route.query.movieId;
      console.log(this.$store.state.username)
      let points
      if(movieId){
        try{
          const whoIAm = await axios.get(`http://127.0.0.1:8000/accounts/mypage/`).then(res => res.data);
          console.log(whoIAm.user)
          points = whoIAm.user.points
          await axios.post(`http://127.0.0.1:8000/community/moviepoints/${movieId}/`, 
          {
            username : whoIAm.user.username,
            password : whoIAm.user.password
          }, 
          {
            headers : {
              Authorization : `jwt ${localStorage.getItem('jwt')}`
            }
          })
          alert('포인트 적립되었습니다 \n현재 포인트 : ' + ( whoIAm.user.points + 1000))
        } catch (error) {
          // aready add point
          alert('이미 포인트를 받았습니다 \n현재 포인트 : ' + points)
        }
      }
    }
  },
  computed: {
    imgSrc: function () {
      return this.movie && this.movie.poster_path ? "https://image.tmdb.org/t/p/original" + this.movie.poster_path : '';
    },
  },
 async created() {
  const movieId = this.$route.query.movieId;
  if (movieId) {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/movies/movies/${movieId}/`);
      this.movie = response.data;
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>