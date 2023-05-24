<template>
  <div>
    <div v-for="giving in givings" :key="giving.id" class="card">
      <img :src="getThumbnailImage(giving)" alt="Giving Image">
      <p>{{ giving.title }}</p>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters(['givings']),
  },
  methods: {
    ...mapActions(['getGivings']),
    getThumbnailImage(giving) {
      // 이미지 링크 배열에서 "thumbnail" 크기의 이미지 링크를 반환합니다.
      const thumbnailImage = giving.image.imagelink.find(link => link.size === 'original');
      if (thumbnailImage) {
        return thumbnailImage.url;
      }
      // "thumbnail" 크기의 이미지가 없는 경우 기본 이미지 URL 또는 다른 크기의 이미지 URL을 반환할 수도 있습니다.
      return giving.image.imagelink[0].url;
    },
  },
  created() {
    this.getGivings();
  },
};
</script>

<style scoped>
.card {
  display: inline-block;
  width: 20%;
  margin: 10px;
  padding: 10px;
  border: 1px solid #ccc;
  text-align: center;
}
.card img {
  width: 100%;
  height: auto;
}
</style>
