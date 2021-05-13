<template>
  <ul id="VideoList" :class="showDetail">
    <VideoListItem 
      v-for="(video,idx) in videos"
      :key="idx"
      :video="video"
    />
  </ul>
</template>

<script>
import VideoListItem from './VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  methods: {},
  computed: {
    videos() {
      return this.$store.state.searchList[0]
    },
    showDetail() {
      if (this.$store.state.showDetail){
        return 'list-group col-4'

      } else {
        return 'list-group col-12'
      }
    }
    
  }
}
</script>

<style>

</style>