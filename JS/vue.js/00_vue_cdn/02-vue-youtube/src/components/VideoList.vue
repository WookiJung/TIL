<template>
  <ul id="VideoList" class="list-group col-4">
    <VideoListItem 
      v-for="video in videos" 
      :key='video.id.videoId' 
      :video="video" 
      @click-youtube="onClickYoutube"
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
  props:{
    videos: Array
  },
  data() {
    return {
      video: {},
      URL: '',
    }
  },
  methods: {
    onClickYoutube(video) {
      this.video = video
      this.$emit('click-youtube', this.video)

    }
  }

}
</script>

<style>

</style>