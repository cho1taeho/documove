<template>
  <div>
    <br>
    <br>
    <br>
    
    <h2>Giving List</h2>
    <div class="giving-list">
      <div v-for="giving in givings" :key="giving.id" class="giving-item">
        <h3>{{ giving.title }}</h3>
        <p>{{ giving.summary }}</p>
        <p>Theme: {{ giving.themeName }}</p>
        <p>Country: {{ giving.country }}</p>
        <p>Region: {{ giving.region }}</p>
        <p>Funding: {{ giving.funding }}</p>
        <p>Remaining: {{ giving.remaining }}</p>
        <p>Number of Donations: {{ giving.numberOfDonations }}</p>
        <p>Status: {{ giving.status }}</p>
        <p>Activities: {{ giving.activities }}</p>
        <p>Approved Date: {{ giving.approvedDate }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'Giving',
  computed: {
    ...mapGetters(['givings']),
  },
  mounted() {
    this.fetchGivings();
  },
  methods: {
    ...mapActions(['getGivings']),
    fetchGivings() {
      this.getGivings();
    }
  }
}
</script>

<style>
.giving-item {
  margin-bottom: 20px;
}
</style>
