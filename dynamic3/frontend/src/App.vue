<template>
  <div id="app">
    <head-bar></head-bar>
    <router-view/>
  </div>
</template>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
</style>

<script>
  import HeadBar from './components/HeadBar'

  export default {
    name: 'App',
    components: {
      HeadBar
    },
    data() {
      return {}
    }
  }
</script>