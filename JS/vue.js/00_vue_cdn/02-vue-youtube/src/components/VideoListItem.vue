<template>
  <li class="list-group-item video-item" @click="onClickThumbnail">
    <img class="me-3" :src="videoImgUrl" alt="video-Thumbnail">
    <div class="media-body d-flex flex-column align-items-start">
      <p>{{ video.snippet.title }}</p>
      <p>{{ video.snippet.channelTitle }}</p>
    </div>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props:{
    video: Object,
  },
  data() {
    return {
      selVideo : {},
    }
  },
  methods:{
    onClickThumbnail() {
      this.selVideo = this.video
      this.$emit('click-youtube', this.selVideo)
      
    }
  },
  computed: {
    videoImgUrl () {
      return this.video.snippet.thumbnails.default.url
    },
    videoUrl (){
      return `https://www.youtube.com/embed/${this.video.id.videoId}`
    },
  }

}
</script>

<style>
  .video-item {
    display: flex;
    cursor: pointer;
  }
  .video-item:hover{
    background-color:#eee;
  }
</style>