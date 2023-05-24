<template>
  <div>
    <br>
    <br>
    <br>
    
    <h2>Giving List</h2>
    <div class="giving-list">
      <GivingCard v-for="giving in givings" :key="giving.id" :giving="giving" />
    </div>
  </div>
</template>

<script>
import GivingCard from '@/components/giving/GivingCard'

export default {
  name: 'Giving',
  computed: {
    givings() {
      return this.$store.getters.givings;
    },
  },
  mounted() {
    this.fetchGivings();
  },
  methods: {
    fetchGivings() {
      this.$store.dispatch('getGivings');
    }
  },
  components: {
    GivingCard
  }
}
</script>
