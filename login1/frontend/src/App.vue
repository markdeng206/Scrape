<template>
  <div id="app">
    <head-bar></head-bar>
    <router-view></router-view>
  </div>
</template>

<script>
  import HeadBar from './components/HeadBar'

  export default {
    components: {
      HeadBar
    }
  }
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
  }
</style>
