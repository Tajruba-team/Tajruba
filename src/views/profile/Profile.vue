<template>
  <div class="profile white">
    <div class="grey lighten-5 userCard">
      <v-btn small absolute left="0" router to="/EditProfile" fab color="white" class="my-3 pt-2 pl-1">
        <v-icon color="primary">fas fa-user-edit</v-icon>
      </v-btn>

      <v-layout column justify-center align-center class="pt-4">
        <v-avatar class="elevation-10" size="95" color="gey">
          <img :src="userAvatar || 'http://s3.amazonaws.com/37assets/svn/765-default-avatar.png'" alt="alt">
        </v-avatar>
        <div class="primary--text mt-3">
          <h2 class="font-weight-bold "> حسان ثابت </h2>
          <p class="font-weight-light ">مطور مواقع</p>
        </div>
      </v-layout>

      <v-tabs fixed xs12 md6 justify-center grow color="transparent" slider-color="primary lighten-5">
        <v-tab active ml-5 router to="/profile/" class="primary--text">
          <span>المزيد </span>
        </v-tab>
        <v-tab active ml-5 router to="/profile/posts" class="primary--text">
          <span>تجاربي</span>
        </v-tab>
        <v-tab active ml-5 router to="/profile/favourites" class="primary--text">
          <span>المفضله</span>
        </v-tab>
      </v-tabs>
    </div>
    <div class="block"></div>
    <v-container>
      <router-view />
    </v-container>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        offsetTop: 0
      }
    },
    computed: {
      userAvatar() {
        return this.$store.getters.userInfo.avatar
      }
    },
    mounted: function () {
      this.$store.state.currentPage = this.$route.name
    },

    methods: {
      onScroll (e) {
        this.offsetTop = e.target.scrollTop
        console.log(this.offsetTop)
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import '../../styles/views/profile/profile';
</style>