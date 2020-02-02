<template>
  <div>
    <i ref="btn"></i>
  </div>
</template>
<script>
  export default {
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
      onHandleGeetest(captchaObj) {
        console.log('success', captchaObj)
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
            // 极验校验的参数，将其传给服务端，进行校验。
            console.log(
              "3，图形验证通过，将数据传递给父组件，进行服务端验证"
            )
            console.log('params', params)
            this.$emit('success', params)
          })
          .onError(function () {
            //   图形验证失败
          })

      },
      initGeetest() {
        this.axios
          .get(
            this.initURL + '?t=' + new Date().getTime()
          )
          .then(({data: data}) => {
            console.log("1,页面初始化，调用极验接口1，进行图形验证码的加载")
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
      show: function () {
        this.captchaObj.verify()
      }
    }
  }
</script>
<style scoped></style>
