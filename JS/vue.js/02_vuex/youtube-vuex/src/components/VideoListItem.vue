<template>
  <li class="list-group-item video-item" @click="watchYoutube">
    <img class="me-3" :src="videoImgUrl" alt="video-Thumbnail">
    <div class="media-body d-flex flex-column align-items-start flex-wrap">
      <p>{{ video.snippet.title }}</p>
      <p>{{ video.snippet.channelTitle }}</p>
      <p>{{ videoPublishDate}}</p>
    </div>
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props:{
    video: Object,
  },
  methods:{
    watchYoutube() {
      console.log(this.video)
      this.$store.dispatch('watchVideo', this.video)
    }
  },
  computed: {
    videoImgUrl () {
      return this.video.snippet.thumbnails.default.url
    },
    videoUrl (){
      return `https://www.youtube.com/embed/${this.video.id.videoId}`
    },
    videoPublishDate() {
      const today = new Date();
      const value = this.video.snippet.publishTime
      const timeValue = new Date(value);

      const betweenTime = Math.floor((today.getTime() - timeValue.getTime()) / 1000 / 60);
      if (betweenTime < 1) return '방금전';
      if (betweenTime < 60) {
          return `${betweenTime}분전`;
      }

      const betweenTimeHour = Math.floor(betweenTime / 60);
      if (betweenTimeHour < 24) {
          return `${betweenTimeHour}시간전`;
      }

      const betweenTimeDay = Math.floor(betweenTime / 60 / 24);
      if (betweenTimeDay < 365) {
          return `${betweenTimeDay}일전`;
      }

      return `${Math.floor(betweenTimeDay / 365)}년전`;
    }
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