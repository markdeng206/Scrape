<template>
  <el-row id="header">
    <el-col class="container" :span="18" :offset="3">
      <el-row>
        <el-col :span="4" class="logo">
          <router-link :to="{name: 'index'}">
            <img src="../assets/logo.png" class="logo-image">
            <span class="logo-title">Scrape</span>
          </router-link>
        </el-col>
      </el-row>
    </el-col>
  </el-row>

</template>

<script>
  export default {
    name: "HeadBar"
  }
</script>

<style scoped lang="scss">
  #header {
    background-color: white;
  }

  .container {
    height: 60px;
    padding-top: 8px;
  }

  .logo {
    height: 40px;
    width: 200px;
    position: relative;

    .logo-image {
      height: 40px;
    }

    .logo-title {
      position: absolute;
      left: 55px;
      top: 5px;
      height: 40px;
      font-size: 23px;
      font-weight: bold;
      color: #444;
    }
  }

  .title {

  }
</style>