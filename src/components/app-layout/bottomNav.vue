<template>
  <v-bottom-nav id="bottom-nav" active.sync="bottomNav" :value="true" fixed shift >
    
    <v-btn color=""
    router to="/">
      <span></span>
      <v-icon>fas fa-flask</v-icon>
    </v-btn>

    <v-btn
     color="primary" 
     router 
     to="/editor">
      <span></span>
      <v-icon >fas fa-feather</v-icon>
    </v-btn>
    
    <v-btn
     color="primary" 
     router to="/profile">
      <span>البروفايل</span>
      <v-icon>fas fa-user</v-icon>
    </v-btn>
    <!-- <v-btn
     color="primary"    
      class="caption" router to="/settings">
      <span>الإعدادات</span>
      <v-icon>fas fa-cog</v-icon>
    </v-btn>
   -->
  </v-bottom-nav>
</template>

<script>
  export default {
    data() {
      return {
        bottomNav: 'home'
      }
    }

  }
</script>

<style>

</style>