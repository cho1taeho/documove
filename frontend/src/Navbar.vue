<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <router-link class="navbar-brand" :to="{ name: 'Home' }">
        <img id="navbar-logo" src="@/assets/images/logo.png" alt="netflix_logo">
      </router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Home' }">홈</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'Giving' }">후원 </router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" @click="toggleThemeSelection">후원 테마</a>
            <div v-show="showThemeSelection" class="theme-selection">          
              <router-link v-for="theme in themes" :key="theme" @click.native="changeTheme(theme)" :to="{ name: 'GivingTheme', query: {theme_id: theme}  }">{{ theme }}</router-link>
            </div>
          </li>
        </ul>
        
        <ul v-if="isLogin" class="navbar-nav">
          <li class="nav-item-right">
            <router-link class="nav-link" :to="{ name: 'MyPage'}">마이페이지</router-link>
          </li>
          <li class="nav-item-right">
            <router-link class="nav-link" @click.native="logout" to="#">로그아웃</router-link>
          </li>
        </ul>

        <ul v-else class="navbar-nav">
          <li class="nav-item-right">
            <router-link class="nav-link" :to="{ name: 'Login' }">로그인</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapState } from 'vuex';

export default {
  name: 'Navbar',
  data() {
    return {
      showThemeSelection: false,
      themes: ['hunger', 'disaster', 'climate', 'agriculture', 'water', 'wildlife', 'justice', 'children']
    };
  },
  methods: {
    ...mapActions(['checkLogin', 'selectTheme']),
    changeTheme(theme) {
      this.selectTheme(theme);
      this.toggleThemeSelection();
    },
    logout() {
      this.$store.dispatch('logout');
    },
    toggleThemeSelection() {
      this.showThemeSelection = !this.showThemeSelection;
    },
    getToken() {
      const token = localStorage.getItem('jwt');
      return token;
    },
    setToken() {
      const token = localStorage.getItem('jwt');
      const config = {
        Authorization: `JWT ${token}`
      };
      return config;
    }
  },
  computed: {
    ...mapState(['isLogin', 'userId'])
  },
  created() {
    this.checkLogin(this.getToken());
  }
};
</script>

<style>
@import './assets/styles/common.css';

.theme-selection {
  position: absolute;
  background-color: #fff;
  padding: 10px;
  border: 1px solid #ccc;
  z-index: 100;
}

.theme-selection a {
  display: block;
  cursor: pointer;
  margin-bottom: 5px;
}
</style>
