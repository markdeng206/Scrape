<template>
  <el-row>
    <el-col :span="18" :offset="3">
      <el-card shadow="hover" class="m-t">
        <div class="text-center p-v-lg">
          <p>
            <img src="../assets/logo.png" class="logo">
          </p>
          <h2 class="text-center">登录成功</h2>
          <div>
            <el-button @click="$router.push({name: 'index'})" type="primary">返回</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>

</template>

<script>
  export default {
    name: 'Success'
  }
</script>

<style scoped>
  .logo {
    width: 200px;
  }
</style>