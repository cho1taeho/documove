<template>
  <div>
    <br>
    <br>
    <br>
    
    <h2>Giving List</h2>
    <div class="theme-buttons">
      <button v-for="theme in themes" :key="theme" @click="filterByTheme(theme)">{{ theme.name }}</button>
    </div>
    <div class="giving-list">
      <div v-for="giving in themeGivings" :key="giving.id" class="giving-item">
        <div class="card" style="width: 18rem;">
          <img :src="giving.image" class="card-img-top" alt="Giving Image">
          <div class="card-body">
            <h5 class="card-title">{{ giving.title }}</h5>
            <p class="card-text">{{ giving.summary }}</p>
            <router-link :to="{ name: 'GivingDetail', params: { id: giving.id }}">View Details</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  name: 'Giving',
  computed: {
    ...mapGetters(['themeGivings']),
  },
  data() {
    return {
      themes: [
        { id: 'climate', name: 'Climate Action' },
        { id: 'env', name: 'Ecosystem Restoration' },
      ],
    };
  },
  methods: {
    ...mapActions(['getGivings', 'setTheme']),
    filterByTheme(theme) {
      this.setTheme(theme.id);
    },
  },
  mounted() {
    this.getGivings();
  },
};
</script>

<style scoped>
.theme-buttons {
  margin-bottom: 20px;
}
.giving-item {
  display: inline-block;
  margin: 10px;
}
</style>