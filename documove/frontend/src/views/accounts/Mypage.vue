<template>
  <div>
    <h1>My Page</h1>
    <p>Point: {{ point }}</p>
    <button @click="increasePoints">A Button</button>
    <button @click="showInputDialog">B Button</button>
    <div v-if="showInput">
      <input type="number" v-model="inputValue" />
      <button @click="submitInput">Submit</button>
      <p v-if="inputValue > point">Points are not enough.</p>
    </div>
    <!-- <p>Input Value: {{ inputValue }}</p> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters(['isLogin']),
    point() {

      return this.$store.state.point;
    },
  },
  methods: {
    ...mapActions(['increasePoints', 'showInputDialog', 'submitInput']),
  },
};
</script>