<template>
  <div>
  </div>
</template>
<script>
  export default {
    name: 'Geetest',
    props: {
      show: {
        type: Boolean,
        default() {
          return false
        }
      }
    },
    data() {
      return {
        initURL: this.$store.state.url.init,
        initData: null,
        captchaObj: null,
      }
    },
    methods: {
      onVerify() {
        if (!this.captchaObj) return
        this.captchaObj.verify()
      },
      onHandleGeetest(captchaObj) {
        console.log('captchddaObj', captchaObj)
        if (!captchaObj) {
          this.initGeetest()
        }
        this.captchaObj = captchaObj
        this.captchaObj
          .onSuccess(() => {
            var result = captchaObj.getValidate()
            let params = {
              geetest_challenge: result.geetest_challenge,
              geetest_validate: result.geetest_validate,
              geetest_seccode: result.geetest_seccode,
              status: this.initData.success,
              type: 'geetest'
            }
            this.$emit('success', params)
          })
          .onError(function () {
          })
      },
      initGeetest() {
        this.axios
          .get(
            this.initURL + '?t=' + new Date().getTime()
          )
          .then(({data: data}) => {
            this.initData = data
            this.$initGeet(
              {
                gt: data.gt,
                challenge: data.challenge,
                product: 'bind',
                offline: !data.success,
                https: true
              },
              this.onHandleGeetest
            )
          })
      }
    },
    computed: {},
    created() {
      // 页面创建，调用函数
      this.initGeetest()
    },
    mounted() {
    },
    watch: {
      show: function (val) {
        if (val !== true) return
        // if captcha not loaded
        if (!this.captchaObj) {
          this.initGeetest()
          setTimeout(() => {
            this.onVerify()
          })
        } else {
          this.onVerify()
        }
      }
    }
  }
</script>
<style scoped></style>
