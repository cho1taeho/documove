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
        ></v-img>
      </template>
      <div class="movie-detail-card">
        <div class="movie-detail-toolbar">
          <v-btn icon dark @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <img id="logo-image" src="@/assets/images/logo.png" />
        </div>
        <div class="movie-detail-body">
          <div class="movie-detail-poster">
            <img :src="imgSrc" alt="포스터 없음">
          </div>
          <div class="movie-detail-info">
            <!-- info header -->
            <div class="movie-detail-upper">
              <div class="movie-detail-info-header">
                <div class="movie-detail-info-header-left">
                  <div class="movie-detail-title">
                    {{ giving.title }}
                  </div>
                  <div
                    v-if="giving.approvedDate"
                    class="movie-release-date"
                  >
                    승인 날짜: {{ giving.approvedDate }}
                  </div>
                  <div v-if="giving.themeName">
                    테마: {{ giving.themeName }}
                  </div>
                </div>
                <div class="movie-detail-info-header-right">
                  <div class="movie-vote">
                    {{ giving.funding }}
                  </div>
                  <img id="movie-star" src="@/assets/images/star.png" />
                </div>
              </div>
              <!-- info summary -->
              <div class="movie-detail-overview-header">
                요약
              </div>
              <hr />
              <div
                v-if="giving.summary"
                class="movie-detail-overview-body"
              >
                {{ giving.summary }}
              </div>
              <div v-else class="movie-detail-overview-body">
                요약 정보가 제공되지 않습니다.
              </div>
            </div>
            <div class="movie-detail-lower">
              <!-- videos -->
              <div class="movie-youtube-area">
                관련 영상
                <hr />
                <YoutubeList :title="giving.title" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </v-dialog>
  </div>
</template>

<script>
import YoutubeList from "@/components/movies/YoutubeList";

export default {
  name: "GivingCard",
  components: {
    YoutubeList,
  },
  props: {
    giving: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      dialog: false,
    };
  },
  computed: {
    imgSrc() {
      return this.giving.imageLink;
    },
  },
};
</script>

<style>
/* Add your custom styles here */
</style>
