<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <router-link class="navbar-brand" :to="{ name: 'ArticleView' }">DOCUMOVE</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="네비게이션 토글">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'ArticleView' }">홈</router-link>
          </li>
          <li v-if="isLogin && !isRegistered" class="nav-item"> 
            <router-link class="nav-link" :to="{ name: 'MyPageView' }">마이 페이지</router-link>
          </li>
          <li v-if="isLogin && !isRegistered" class="nav-item"> 
            <a class="nav-link" href="#" @click="logout">로그아웃</a>
          </li>
          <li v-if="!isLogin || isRegistered" class="nav-item">
            <router-link class="nav-link" :to="{ name: 'LogInView' }">로그인</router-link>
          </li>
          <li v-if="!isLogin || isRegistered" class="nav-item"> 
            <router-link class="nav-link" :to="{ name: 'SignUpView' }">회원가입</router-link>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    isSignUp() {
      return this.$route.name === 'SignUpView'
    },
    isRegistered() {
      return this.$store.state.isRegistered
    }
  },
  methods: {
    logout() {
      this.$store.commit('CLEAR_TOKEN') 
      if (this.$route.name !== 'ArticleView') {     
        this.$router.push({name:'ArticleView'})}
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

@media (max-width: 768px) {
  .navbar-toggler {
    display: block;
  }

  .navbar-collapse {
    display: none;
  }

  .navbar-collapse.show {
    display: block;
  }

  .navbar-nav {
    flex-direction: column;
    align-items: flex-start;
    background-color: #343a40;
    padding: 10px;
    margin-top: 10px;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    width: auto;
  }

  .navbar-nav li {
    margin-bottom: 10px;
  }

  .navbar-nav li:last-child {
    margin-bottom: 0;
  }
}
</style>