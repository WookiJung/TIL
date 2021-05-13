<template>
  <div class="container">
    <h1>Youtube Browser</h1>
    <SearchBar />
    <div class="row">
      <VideoDetail v-if="showDetail" />
      <VideoList />
    </div>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'

export default {
  name: 'App',
  components: {
    SearchBar, VideoList, VideoDetail,
  },
  methods: {},
  computed: {
    showDetail(){
      return this.$store.state.showDetail
    }
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
  margin-top: 60px;
}
</style>
