<template>
  <div class="col-8">
    <iframe width="100%" height="100%" :src="videoUrl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <div>
      <h4>{{ videoTitle }}</h4>
      <p>{{ videoDescription }}</p>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props:{
    video: Object
  },

  computed:{
    videoUrl(){return `https://www.youtube.com/embed/${this.video.id.videoId}`},
    videoTitle(){return `${this.video.snippet.title}`},
    videoDescription() {return `${this.video.snippet.description}`}
  
  }
}
</script>

<style>

</style>