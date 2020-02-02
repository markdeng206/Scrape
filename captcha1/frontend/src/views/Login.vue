<template>
  <el-row>
    <el-col :span="18" :offset="3">
      <el-card shadow="hover" class="m-t">
        <el-row>
          <el-col :span="10" :offset="7">
            <el-form :model="form" label-width="80px">
              <h2>登录</h2>
              <el-form-item label="用户名">
                <el-tooltip class="item" effect="dark" content="admin" placement="right">
                  <el-input v-model="form.username"></el-input>
                </el-tooltip>
              </el-form-item>
              <el-form-item label="密码">
                <el-tooltip class="item" effect="dark" content="admin" placement="right">
                  <el-input v-model="form.password" type="password"></el-input>
                </el-tooltip>
              </el-form-item>
              <el-form-item>
                <geetest :show="verify" @success="onSuccessCaptcha"></geetest>
                <el-button type="primary" @click="onSubmit">登录</el-button>
              </el-form-item>
            </el-form>
          </el-col>
        </el-row>
      </el-card>
    </el-col>
  </el-row>
</template>

<script>
  import store from '../store'
  import Geetest from '../components/Geetest'

  export default {
    name: 'Login',
    data() {
      return {
        verify: false,
        verified: false,
        form: {
          username: null,
          password: null,
          captcha: {}
        },
      }
    },
    components: {
      Geetest
    },
    methods: {
      onSubmit() {
        if (!this.verified) {
          // show captcha if first time
          this.verify = true
          return
        }
        this.$http.post(store.state.url.login, this.form)
          .then(({status: status, data: data}) => {
            // login success
            if (status == 200) {
              this.$message.success(data)
              this.$router.push({name: 'success'})
            }
          })
          .catch(({response: {status: status, data: data}}) => {
            // show error message
            this.$message.error(data)
          })
      },
      onSuccessCaptcha(params) {
        Object(this.form.captcha, params)
        this.$set(this.form, 'captcha', params)
        this.verified = true
        this.verify = false
        console.log('verified successfully')
        this.onSubmit()
      }
    }
  }
</script>

<style scoped>
  form {
    margin-top: 80px;
    margin-bottom: 60px;
  }

  h2 {
    text-align: center;
    margin-bottom: 20px;
  }
</style>