<template>
  <div id="index">
    <el-row class="m-t">
      <el-col :span="18" :offset="3">
        <el-row v-loading="loading" v-if="!books">
        </el-row>
        <el-row :gutter="15">
          <el-col :span="4" v-for="book in books" :key="book.id">
            <el-card shadow="hover" class="item m-b" v-loading="loading">
              <el-row class="top">
                <el-col :span="24">
                  <router-link :to="{ name: 'detail', params: { id: book.id }}">
                    <img :src="'/api/proxy/' + book.cover" class="cover">
                  </router-link>
                </el-col>
              </el-row>
              <el-row class="bottom p-t-none">
                <el-col :span="24">
                  <router-link :to="{ name: 'detail', params: { id: book.id }}">
                    <h3 class="m-b-sm">{{ book.name }}</h3>
                  </router-link>
                </el-col>
              </el-row>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="10" :offset="11">
        <div class="pagination m-v-lg">
          <el-pagination
              background
              @current-change="onPageChange"
              :current-page.sync="page"
              :page-size="limit"
              layout="total, prev, pager, next"
              :total="total">
          </el-pagination>
        </div>
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
        total: null,
        page: parseInt(this.$route.params.page || 1),
        limit: 18,
        books: null
      }
    },
    mounted() {
      this.onFetchData()
    },
    methods: {
      onPageChange(page) {
        this.$router.push({
          name: 'indexPage',
          params: {
            page: page
          }
        })
        this.onFetchData()
      },
      onFetchData() {
        this.loading = true
        this.$axios.get(this.$store.state.url.index, {
          params: {
            limit: this.limit,
            offset: (this.page - 1) * this.limit
          }
        }).then(({data: {results: results, count: total}}) => {
          this.loading = false
          this.books = results
          this.total = total
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
</style>
<style lang="scss" scoped>
  .item {
    $height: 350px;
    width: 100%;
    height: $height;

    .top {
      width: 100%;
      height: $height - 80px;

      .cover {
        width: 100%;
        height: $height - 80px;
      }
    }

    .bottom {
      font-size: 14px;
      height: 80px;
      padding: 10px;
    }

  }

  .pagination {
    float: right;
  }
</style>