<template>
  <div class="home">
    <categories-list class="mb-2" />
    <v-container class="pt-0  mb-5">
      <div class="cardsHolder mt-3">
        <v-flex ms12 class="mt-1 mb-3" v-for="tejruba in FilterdExperiences" :key="tejruba.ID">

          <v-card class="elevation-2 article_card mt-0" router :to="`/postPage/${tejruba.ID}`" max-width="800">
            <v-img :src="tejruba.Img" aspect-ratio="2.75">
              <v-layout justify-start>
                <v-avatar class="box-shadow pa-3 ma-2" size="40" color="gray">
                  <img class="elevation-15" src="../../assets/img/avatar.png" alt="alt">
                </v-avatar>
              </v-layout>
            </v-img>

            <v-card-title primary-title class="text-xs-right">
              <div>
                <h2 class="" ma-0>{{ tejruba.Title }}</h2>
              </div>
            </v-card-title>
            <v-card-text class="pt-0">
              <p class="grey--text row-4 text-xs-right mb-0 caption"> {{ tejruba.content | truncate }} <span class="font-weight-bold">. . .</span></p>
            </v-card-text>
            <div class="caption ml-0 mb-2 mx-3 text-xs-right">
              {{ tejruba.Date }}
            </div>
            <v-divider></v-divider>
            <v-layout row align-center class="py-0">
              <v-flex class="text-xs-right caption">
                <span class="mx-3"><span>5</span> تعليقات</span>
                <span><span>{{ tejruba.Likes }}</span> الاعجاب</span>
              </v-flex>
              <v-spacer></v-spacer>
              <v-btn fab icon small flat color="primary" dark>
                <v-icon>fas fa-bookmark</v-icon>
              </v-btn>
            </v-layout>
          </v-card>
        </v-flex>
      </div>
    </v-container>
  </div>
</template>


<script>
  import categoriesList from "../../components/CategoriesList.vue"
  import {
    mapGetters
  } from 'vuex'
  import {
    connect
  } from 'net';

  export default {
    name: "home",
    components: {
      categoriesList,
    },
    data() {
      return {

      }
    },

    computed: {
      ...mapGetters(['altejarub', 'contents', 'textContent', 'sideNav']),
      FilterdExperiences() {
        if (this.$store.state.experienceFilterValue) {
          return this.altejarub.filter((exp) => {
            return exp.Category === this.$store.state.experienceFilterValue;
          })
        } else {
          return this.altejarub
        }
      }

    },

    methods: {
      test: function () {
        console.log(store)
      }
    },

    mounted: function () {
      this.$store.state.currentPage = this.$route.name;
      console.log(this.$store.state.currentPage);
      // console.log(this.$route.name); 
    },

    filters: {
      truncate(value) {
        if (!value) return ''
        value = value.toString()
        var content = value.trim()
        content = content.split(' ').slice(0, 50)
        content = content.join(' ')
        value = content
        console.log('...>>>  ', value)
        return value
      },
    }

  }
</script>

<style lang="scss" scoped>
  @import '../../styles/views/Home';
</style>