<template>
  <div class="col-8">
    <div class="ratio ratio-16x9">
      <iframe width="100%" height="100%" :src="videoUrl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
    <div class="mt-3">
      <h4>{{ videoTitle }}</h4>
      <p class="mt-3 p-2 fs-5">{{ videoChannel }}</p>
      <p class="flex-wrap m-3">{{ videoDescription }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  computed:{
    videoUrl(){return `https://www.youtube.com/embed/${this.$store.state.watchVideo.id.videoId}`},
    videoTitle(){return `${this.$store.state.watchVideo.snippet.title}`},
    videoDescription() {return `${this.$store.state.watchVideo.snippet.description}`},
    videoChannel() {return `${this.$store.state.watchVideo.snippet.channelTitle}`},
  }
}
</script>

<style>

</style>