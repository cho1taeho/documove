<template>
  <div id="app">
    <Navbar/>
    <!-- <v-app>
      <DonationCard : topDonator="topDonator"/> -->
      <transition name="fade">
        <router-view/>
      </transition>
    <!-- </v-app> -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Navbar from '@/Navbar'
// import DonationCard from '@/components/community/DonationCard'


export default {
  name: 'App',
  data() {
    return {
      windowHeight: window.innerHeight,
    }
  },
  components: {
    Navbar,
    // DonationCard
  },
  computed: {
    ...mapActions([
      'checkMovies',
      'checkLogin'
    ]),
    ...mapGetters([
      // 'topDonator'
    ])
  },
  methods: {
    getToken() {
      const token = localStorage.getItem('jwt')
      return token
    },
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    ...mapActions([
      // 'fetchTopDonator'
    ])
  },
  created() {
    this.$store.dispatch('checkLogin', this.getToken())
    // this.fetchTopDonator()
  },
}

</script>

<style>
  @import './assets/styles/common.css';
  @import './assets/styles/font.css';
  @import './assets/styles/navbar.css';
  @import './assets/styles/button.css';
  /* @import './assets/styles/tinder.css'; */
  @import './assets/styles/youtube.css';
  @import './assets/styles/moviecard.css';
</style>
