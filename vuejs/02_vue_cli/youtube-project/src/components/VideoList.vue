<template>
  <ul>
    <video-list-item></video-list-item>
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'


export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>

</style>
