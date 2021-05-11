<template>
  <div class="container">
    <h1>Youtube Browser</h1>
    <SearchBar @fetch-videos="onFetchVideos" />
    <div class="row">
      <VideoDetail :video="video" v-if="showDetail" />
      <VideoList 
      :videos="videos" :showDetail="showDetail"
      @click-youtube="onClickYoutube"
       />
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
  data() {
    return {
      videos: [],
      video: {},
      showDetail: false,
    }
  },
  methods:{
    onFetchVideos(videos) {
      //console.log(videos) // videos는 res.data.items
      this.videos = videos
    },
    onClickYoutube(video) {
      this.video = video
      this.showDetail = true
    }
  }
}
</script>

<style>

</style>