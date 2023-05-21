<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView'}"> [CREATE] </router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/article/ArticleList.vue.js'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  created() {
    this.$store.dispatch('getArticles')
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style>
</style>