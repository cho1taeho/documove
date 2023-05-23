<template>
  <div>
    <h1>Donate</h1>
    <form @submit.prevent="donate">
      <label for="amount">Donation Amount:</label>
      <input type="number" id="amount" v-model="donationAmount" :max="userPoints">
      <button type="submit">Donate</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      donationAmount: 0
    }
  },
  computed: {
    userPoints() {
      return this.$store.getters.getUserPoints
    }
  },
  methods: {
    donate() {
      if (this.donationAmount <= this.userPoints) {
        const donationData = {
          points: this.donationAmount
        }
        this.$axios.post('/api/donate/', donationData)
          .then(response => {
            const donatedPoints = response.data.donatedPoints
            this.$store.commit('updateUserPoints', donatedPoints)
            // 성공 메시지 표시 또는 다른 처리
          })
          .catch(error => {
            // 에러 메시지 표시 또는 다른 처리
          })
      } else {
        // 에러 메시지 표시: 후원 금액이 사용자 포인트를 초과함
      }
    }
  }
}
</script>

<style scoped>
/* Add custom styles as needed */
</style>