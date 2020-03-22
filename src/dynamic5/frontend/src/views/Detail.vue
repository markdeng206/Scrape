<template>
  <div id="detail" class="m-t">
    <el-row>
      <el-col :span="18" :offset="3">
        <el-card shadow="hover" v-loading="loading">
          <el-row class="item" v-if="book">
            <el-col :xs="0" :sm="8">
              <router-link :to="{ name: 'detail', params: { id: book.id }}">
                <img :src="book.cover" class="cover">
              </router-link>
            </el-col>
            <el-col :xs="16" :sm="12" class="p-h">
              <router-link :to="{ name: 'detail', params: { id: book.id }}">
                <h2 class="m-b-sm">{{ book.name }} - {{ book.alias }}</h2>
              </router-link>
              <div class="categories">
                <el-button class="category" size="mini" type="primary" :key="category"
                           v-for="category in book.categories">{{ category }}
                </el-button>
              </div>
              <div class="m-v-sm info">
                <span>{{ book.regions.join('、') }}</span>
                <span> / </span>
                <span>{{ book.minute }} 分钟</span>
              </div>
              <div class="m-v-sm info">
                <span>{{ book.published_at }} 上映</span>
              </div>
              <div class="drama">
                <h3>剧情简介</h3>
                <p>
                  {{ book.drama }}
                </p>
              </div>
            </el-col>
            <el-col :xs="8" :sm="4">
              <p class="score m-t-md m-b-n-sm">{{ book.score.toFixed(1) }}</p>
              <p>
                <el-rate
                    :value="book.score / 2"
                    disabled
                    :max="5"
                    text-color="#ff9900">
                </el-rate>
              </p>
              <p class="m-t-lg">
                <el-button size="small" type="primary" @click="onBuy">
                  购票选座
                </el-button>
              </p>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
    <el-row v-if="book">
      <el-col :span="18" :offset="3">
        <h2 class="subtitle">导演</h2>
        <el-row :gutter="15" class="directors">
          <el-col :span="4" v-for="director in book.directors" class="director" :key="director.name">
            <el-card shadow="hover">
              <img :src="director.image" class="image">
              <p class="name text-center m-b-none m-t-xs">{{ director.name }}</p>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-row v-if="book">
      <el-col :span="18" :offset="3">
        <h2 class="subtitle">演员</h2>
        <el-row :gutter="15" class="actors">
          <el-col :span="4" v-for="actor in book.actors" class="actor" :key="actor.name">
            <el-card shadow="hover" class="m-b">
              <img :src="actor.image" class="image">
              <el-tooltip class="item" effect="dark" :content="actor.name" placement="right">
                <p class="name text-center m-b-none m-t-xs">{{ actor.name }}</p>
              </el-tooltip>
              <el-tooltip class="item" effect="dark" :content="actor.role" placement="right">
                <p class="role text-center m-b-none m-t-xs">饰：{{ actor.role }}</p>
              </el-tooltip>
            </el-card>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
    <el-row v-if="book">
      <el-col :span="18" :offset="3">
        <h2 class="subtitle">剧照</h2>
        <el-row :gutter="15" class="photos">
          <el-col :span="3" v-for="photo in book.photos" class="photo" :key="photo">
            <el-card shadow="hover" class="m-b">
              <el-image :src="photo" fit="cover" lazy :preview-src-list="photos"></el-image>
            </el-card>
          </el-col>
        </el-row>
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
    computed: {
      photos: {
        get() {
          return this.book.photos.map(photo => photo.replace(/(.*[(?:jpg)|(?:png)]).*/, '$1'))
        }
      }
    },
    methods: {
      onBuy() {
        window.location = 'https://maoyan.com/'
      },
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
  }

  $color-primary: #E9415A;

  .item {
    width: 100%;

    .categories {
      .category {
        padding: 5px 10px;
      }
    }

    .cover {
      width: 100%;
    }

    .info {
      font-size: 14px;
    }

    .score {
      color: #ffb400;
      font-size: 40px;
      font-weight: bold;
    }

    .drama {
      h3 {
        border-left: 3px solid $color-primary;
        padding-left: 8px;
      }

      p {
        font-size: 15px;
        line-height: 24px;
        color: #444;
      }
    }
  }

  .subtitle {
    border-left: 3px solid $color-primary;
    padding-left: 8px;
  }

  .directors {
    .director {
      .image {
        width: 100%;
      }
    }
  }

  .actors {
    .actor {
      height: 272px;

      .image {
        width: 100%;
      }

      .name {
        font-size: 14px;
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
      }

      .role {
        font-size: 14px;
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
      }
    }
  }

  .photos {
    .photo {
      .image {
        width: 100%;
      }
    }
  }

</style>