<template>
  <div class="col-mb-6 docu-item">
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      <template v-slot:activator="{ on, attrs }">
      <v-img
        :src="imgSrc" alt="포스터 없음"
        v-bind="attrs"
        v-on="on"
      >
      </v-img>
    </template>
    <div class="docu-detail-card">
      <div class="docu-detail-toolbar">
        <v-btn
          icon
          dark
          @click="dialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
        <img id="logo-image" src="@/assets/images/logo.png"/>
      </div>
      <div class="docu-detail-body">
        <div class="docu-detail-poster">
          <img :src="imgSrc" alt="포스터 없음">
        </div>
        <div class="docu-detail-info">
          <!-- info header -->
          <div class="docu-detail-upper">
            <div class="docu-detail-info-header">
              <div class="docu-detail-info-header-left">
                <div class="docu-detail-title">
                  {{ docu.title }}
                </div>
                <div
                v-if="docu.release_date"
                class="docu-release-date">
                  개봉  :  {{ docu.release_date }}
                </div>
                <div
                v-if="docu.genre_ids">
                  <!-- {{ docu.genre_ids }} -->
                </div>
              </div>
              <div class="docu-detail-info-header-right">
                <div class="docu-vote">
                  {{ docu.vote_average }}
                </div>
                <img id="docu-star" src="@/assets/images/star.png">
              </div>
            </div>
            <!-- info overview -->
            <div class="docu-detail-overview-header">
              줄거리
            </div>
            <hr>
            <div
              v-if="docu.overview"
              class="docu-detail-overview-body">
              {{ docu.overview }}
            </div>
            <div v-else
              class="docu-detail-overview-body">
              해당 영화는 줄거리가 제공되지 않습니다.
            </div>
          </div>
          <div class="docu-detail-lower">
            <!-- youtube -->
            <div class="docu-youtube-area">
              관련 영상
              <hr>
              <YoutubeList :title="docu.title"/>
            </div>
          </div>
        </div>
      </div>
    </div>
    </v-dialog>
  </div>
</template>

<script>
import YoutubeList from '@/components/docus/YoutubeList'

export default {
  name: 'DocuCard',
  components: {
    YoutubeList
  },
  props: {
    docu: {
      type: Object,
      required: true
    },
  },
  data() {
    return {
      dialog: false,
      notifications: false,
      sound: true,
      widgets: false,
    }
  },
  computed: {
    imgSrc: function () {
      return "https://image.tmdb.org/t/p/original" + this.docu.poster_path
    },
  },
}
</script>

<style>

</style>
