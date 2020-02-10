<template>
  <div id="index" v-infinite-scroll="onLoadMore" infinite-scroll-disabled="disabled">
    <el-row>
      <el-col :span="18" :offset="3" class="m-b-lg">
        <el-card v-for="item in news" shadow="hover" class="item m-t" :key="item.code">
          <el-row>
            <el-col :xs="item.thumb? 15: 24" :sm="item.thumb? 18: 24" :md="item.thumb? 20: 24">
              <h3 class="m-l-md m-t-md">
                <el-button size="mini" type="primary" class="website m-t-n-xs">{{ item.website }}</el-button>
                <a :href="item.url" target="_blank" class="m-l-sm">{{ item.title }}</a>
              </h3>
              <p class="info m-l-md">
                <span>{{ item.published_at | moment('timezone', 'Asia/Shanghai', 'YYYY-MM-DD HH:mm:ss') }}
                </span>
                <span class="m-l" v-if="item.source && item.source !== item.website">来源： {{ item.source }}</span>
              </p>
            </el-col>
            <el-col :xs="9" :sm="6" :md="4" class="text-center" v-if="item.thumb">
              <div class="thumb">
                <img :src="item.thumb">
              </div>
            </el-col>
          </el-row>
        </el-card>
        <el-card class="item item-flat m-t" shadow="never" v-loading="loading" v-if="!disabled"></el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'Index',
    components: {},
    data() {
      return {
        loading: false,
        count: null,
        page: parseInt(this.$route.params.page || 1),
        limit: 10,
        news: null,
        previous: null,
        next: null,
      }
    },
    computed: {
      disabled() {
        return !this.next
      }
    },
    mounted() {
      this.onFetchData()
    },
    methods: {
      onLoadMore() {
        this.page += 1
        this.onFetchData()
      },
      onFetchData() {
        this.loading = true
        this.$axios.get(this.$store.state.url.index, {
          params: {
            limit: this.limit,
            offset: (this.page - 1) * this.limit
          }
        }).then(({data: {results: results, count: count, next: next, previous: previous}}) => {
          this.loading = false
          this.previous = previous
          this.next = next
          this.news = this.news ? this.news.concat(results) : results
          this.count = count
        })
      }
    }
  }
</script>

<style lang="scss">
  .item {
    .el-card__body {
      padding: 0;
    }
  }

  #index {
    height: 1000px;
    overflow: auto;
  }
</style>
<style lang="scss" scoped>
  .item {
    $height: 110px;
    width: 100%;
    height: $height;

    &.item-flat {
      height: $height;
    }

    .website {
      position: relative;
      top: -2px;
      padding: 6px 10px;
    }

    .info {
      font-size: 14px;
      color: #666;
    }

    .thumb {
      $margin: 0px;
      width: 160px;
      float: right;
      margin-right: $margin;
      margin-top: $margin;
      height: $height - $margin * 2;
      overflow: hidden;
      position: relative;

      img {
        max-width: 100%;
        min-height: 100%;
        position: absolute;
        left: 0;
        top: 0;
      }
    }
  }

</style>