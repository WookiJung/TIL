<template>
  <div id="app">
    <div id="nav">
      <RouterLink to="/">Home</RouterLink> |
      <RouterLink :to="{name: 'List'}">Articles</RouterLink>
      <RouterLink v-if="!isLoggedIn" :to="{name: 'Login'}">| Login</RouterLink>
      <RouterLink v-if="isLoggedIn" :to="{name: 'Create'}">| Create  </RouterLink> 
      <RouterLink v-if="isLoggedIn" :to="{name: 'Logout'}">| Logout</RouterLink>
    </div>
    <router-view/>
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn',])
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
