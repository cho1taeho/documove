<!-- MyPage.vue -->
<template>
  <div>
    <h1>{{ user.username }}'s Page</h1>
    <img :src="user.badge" alt="badge" />
    <p>Points: {{ user.points }}</p>

    <h2>Wishlist</h2>
    <ul>
      <li v-for="wishlistItem in wishlist" :key="wishlistItem.id">
        {{ wishlistItem.movies.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: {
    ...mapState(['user', 'wishlist'])
  },
  methods: {
    ...mapActions(['fetchUser']),
  },
  created() {
    this.fetchUser(this.$route.params.username);
  }
}
</script>

<style scoped>
/* 필요한 CSS 스타일을 여기에 추가하세요 */
</style>
