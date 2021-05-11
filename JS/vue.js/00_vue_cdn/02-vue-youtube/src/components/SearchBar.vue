<template>
  <div class="search-bar-div">
    <input class="search-bar-input" @input="onInput" @change="onChange" type="text">
  </div>
</template>

<script>

import axios from 'axios'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const SearchURL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'SearchBar',
  data() {
    return {
      query: '',
    }
  },
  methods: {
    onInput(event){
      this.query = event.target.value
    },

    onChange() {
      axios.get(SearchURL, {
        params: {
          key : API_KEY,
          type: 'video',
          part: 'snippet',
          q: this.query,
          }
      })
      .then(res => this.$emit('fetch-videos', res.data.items))
      .catch(err => console.eror(err))
    }
  }
}
</script>

<style>
.search-bar-div {
  text-align: left;
  margin: 20px;
}
.search-bar-input {
  width: 75%;
}
</style>