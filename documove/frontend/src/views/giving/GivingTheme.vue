<template>
  <div>
    <button @click="getGivings">Load Givings</button>
    <ul>
      <li v-for="giving in givings" :key="giving.id">{{ giving.title }}</li>
    </ul>
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
  },
};
</script>