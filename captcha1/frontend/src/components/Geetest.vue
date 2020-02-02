<template>
  <div>
  </div>
</template>
<script>
  export default {
    name: 'Geetest',
    props: {
      // verified: {
      //   type: Boolean,
      //   default() {
      //     return false
      //   }
      // }
    },
    data() {
      return {
        initURL: this.$store.state.url.init,
        initData: null,
        captchaObj: null,
        verified: false
      }
    },
    methods: {
      onVerify() {
        if (this.verified) return
        if (!this.captchaObj) {
          this.initGeetest()
          console.log('reinit captcha')
          setTimeout(() => {
            console.log('verifying...')
            this.captchaObj.verify()
          }, 2000)
        } else {
          console.log('verifying...')
          this.captchaObj.verify()
        }
      },
      onHandleGeetest(captchaObj) {
        console.log('init captchaObj', captchaObj)
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
            this.verified = true
            this.$emit('success', params)
          })
          .onError(function () {
            this.verified = false
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
    mounted() {
      this.initGeetest()
    }
  }
</script>
<style scoped></style>
