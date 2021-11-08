<template>
  <div id="app">
    <h1>My first Youtube Project</h1>
    <header>
      <the-search-bar @input-change="onInputChange"></the-search-bar>
    </header>
    <section>
      <video-list :videos="videos"></video-list>
    </section>
  </div>
</template>

<script>
import TheSearchBar from '@/components/TheSearchBar'
import axios from 'axios'


const API_KEY = 'AIzaSyBcIRuptEl7L0hMMSsrYlyU-gCKMfno9LE'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    TheSearchBar,
  },
  data: function () {
    return {
      inputValue: null,
      videos: [],
    }
  },
  methods: {
    onInputChange: function (inputValue) {
      //console.log(inputValue)
      this.inputValue = inputValue

      const params = {
        key: API_KEY,
        part: 'snippet',
        q: this.inputValue,
        type: 'video',
      }
      axios({
        method: 'get',
        url: API_URL,
        params,
      })
      .then(res => {
        console.log(res)
        this.videos = res.data.items
      })
      .catch(err => {
        console.log(err)
      })
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
