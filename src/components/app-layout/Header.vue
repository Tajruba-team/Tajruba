<template>
    <div class="toolbar">
        <v-toolbar  color="white" id="toolbar" class="hidden-md-and-up">
            <!-- logo -->
            
            <v-toolbar-title align-center justify-start>
                <v-layout row align-center hidden-md-and-up>
                    <img src="../../assets/img/T_logo.svg" class="ml-2 " height="35px" />
                    <v-divider vertical></v-divider>
                    <span class="primary--text caption mr-2">{{ currentPage }}</span>
                </v-layout>
            </v-toolbar-title>
            <!-- pageName -->
        
            <v-spacer></v-spacer>

            <!-- Avatar -->
            <v-avatar size="33" color="primary">
                <img :src="userAvatar || 'http://s3.amazonaws.com/37assets/svn/765-default-avatar.png'" alt="avatar">
            </v-avatar>
        </v-toolbar>
    </div>
</template>



<script>
    export default {
        data() {
            return {
                drawer: this.$store.state.sideNav
            }
        },
        computed: {
            currentPage() {
                return this.$store.state.currentPage
            },
            userAvatar() {
                return this.$store.getters.userInfo.avatar
            },
            sideNav(){
                return this.$store.state.sideNav
            }
        },
        methods:{
            toggleSideNav(){
                this.$store.commit('ToggleSideNav')
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import '../../styles/components/app-layout/Header';
</style>