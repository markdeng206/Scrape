<template>
  <div id="detail" class="m-t">
    <el-row>
      <el-col :span="18" :offset="3">
        <el-card shadow="hover" v-loading="loading">
          <el-row class="item" v-if="book">
            <el-col :xs="16" :sm="16" class="p-h">
              <router-link :to="{ name: 'detail', params: { id: book.id }}">
                <span v-if="book.score" class="score m-r">
                  <i class="el-icon-medal"></i>
                  {{ book.score }}
                </span>
                <h2 class="m-b-sm name">{{ book.name }}</h2>
              </router-link>
              <p v-if="book.introduction" class="introduction">
                简介：{{ book.introduction.length > 100 ? book.introduction.substring(0, 100) + '...' : '' }}
              </p>
              <div class="tags">
                <el-button v-for="tag in book.tags.slice(0, 5)" type="primary" size="mini">
                  {{ tag }}
                </el-button>
              </div>
              <div class="info">
                <p v-if="book.price" class="price">
                  定价：<span>{{ book.price }}</span>
                </p>
                <p v-if="book.authors && book.authors.length > 0" class="authors">
                  作者：{{ book.authors.join('、')}}
                </p>
                <p v-if="book.translators && book.translators > 0" class="translators">
                  译者：{{ book.translators.join('、')}}
                </p>
                <p v-if="book.published_at" class="published-at">
                  出版时间：{{ book.published_at | formatDate }}
                </p>
                <p v-if="book.publisher" class="publisher">
                  出版社：{{ book.publisher }}
                </p>
                <p v-if="book.page_number" class="page-number">
                  页数：{{ book.page_number }}
                </p>
                <p v-if="book.isbn" class="isbn">
                  ISBM：{{ book.isbn }}
                </p>
              </div>
            </el-col>
            <el-col :xs="0" :sm="8">
              <router-link :to="{ name: 'detail', params: { id: book.id }}">
                <img :src="book.cover" class="cover">
              </router-link>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>

    <el-row class="m-t">
      <el-col :span="18" :offset="3">
        <el-card shadow="hover" v-loading="loading">
          <el-row>
            <el-col :span="24" class="p-h">
              <h2 class="title">评价</h2>
              <div class="comments">
                <p v-for="comment in book.comments" class="comment">
                  {{ comment.content }}
                </p>
              </div>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>

    <el-row class="m-t">
      <el-col :span="18" :offset="3">
        <el-card shadow="hover" v-loading="loading">
          <el-row>
            <el-col :span="24" class="p-h">
              <h2 class="title">目录</h2>
              <div class="catalog">
                <pre>{{ book.catalog }}</pre>
              </div>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  const format = require('string-format-obj')
  export default {
    name: 'Detail',
    data() {
      return {
        loading: false,
        id: this.$route.params.id,
        book: null
      }
    },
    mounted() {
      this.onFetchData()
    },
    computed: {},
    methods: {
      onFetchData() {
        this.loading = true
        this.$axios.get(format(this.$store.state.url.detail, {
          id: this.id
        })).then(({data: data}) => {
          this.loading = false
          this.book = data
        })
      }
    }
  }
</script>

<style lang="scss">
  #detail {
    .directors, .actors {
      .el-card__body {
        padding: 15px;
      }
    }

    .photos {
      .el-card__body {
        padding: 0px;
      }

      .el-image {
        display: inherit;
      }
    }

  }
</style>

<style lang="scss" scoped>
  #detail {
    padding-bottom: 50px;

    .el-card {
      min-height: 80px;
    }
  }

  $color-primary: #E9415A;

  .item {
    width: 100%;

    .introduction {
      color: #666;
    }

    .cover {
      width: 100%;
    }

    .name {
      display: inline-block;
    }

    .score {
      display: inline-block;
      color: #ffb400;
      font-size: 30px;
      font-weight: bold;
    }

    .info {
      color: #666;
      font-size: 15px;

      .price > span {
        color: #E9415A;
        font-size: 20px;
      }
    }
  }

  .title {
    border-left: 4px solid #E9415A;
    padding-left: 10px;
    margin-bottom: 20px;
  }

  .catalog {
    display: block;
    unicode-bidi: embed;
    font-family: monospace;
    white-space: pre;
    line-height: 25px;
    font-size: 15px;
  }

  .comments {
    .comment {
      color: #666;
      padding-top: 16px;
      font-size: 15px;
      padding-left: 5px;
      padding-bottom: 15px;
      border-bottom: 1px dashed #EEE;
      margin: 0;

      &:hover {
        background: #EFEFEF;
      }
    }
  }

</style>