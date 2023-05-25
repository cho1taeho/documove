<template>
  <div>
    <br>
    <h1>My Page - {{ user.user.username }}</h1>
    <p>Point: {{ user.user.points }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {},
    }
  },
  async created() {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/accounts/mypage/`);
      this.user = response.data;
      
    } catch (error) {
      console.error(error);
    }
  },
  // methods: {
  //   submitInput() {
  //     if (this.inputValue <= this.user.points) {
  //       console.log('Points are enough. Logic goes here.');
  //     } else {
  //       console.log('Points are not enough.');
  //     }
  //   }
  // }
}
</script>
