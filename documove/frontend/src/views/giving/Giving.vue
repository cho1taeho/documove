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
      const thumbnailImage = giving.image.imagelink.find(link => link.size === 'original');
      if (thumbnailImage) {
        return thumbnailImage.url;
      }      
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
