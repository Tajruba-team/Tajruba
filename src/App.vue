<template>
  <!-- 
                  #تعديلات مهمه #
   [جعل كمبوننت المعلومات يظهر مباشره عند فتح البروفايل] # 
   [جعل كمبوننت المعلومات يظهر مباشره عند فتح البروفايل] # 
-->
  <div id="app">
    <v-app>
      <v-content>
      <side-nav />
        <Header />
        <router-view />
      </v-content>
      <bottom-nav />
    </v-app>
  </div>
</template>

<script>
  import bottomNav from './components/app-layout/bottomNav.vue'
  import sideNav from './components/app-layout/SideNav.vue'
  import Header from './components/app-layout/Header.vue'
  export default {
    components: {
      bottomNav,
      Header,
      sideNav,
    }
  }
</script>
<style lang="scss">
  @import './styles/app';
</style>