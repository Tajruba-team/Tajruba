<template>
    <div>
        <!-- <v-hover v-slot:default="{ hover }"> -->
        <v-navigation-drawer
         right 
         app 
         width="220"
         >
            <v-toolbar flat class="transparent">
                <v-list class="pa-0" >
                    <v-list-tile avatar> 
                        <v-list-tile-avatar>
                            <img src="../../assets/img/T_logo.svg">
                        </v-list-tile-avatar>

                        <v-list-tile-content>
                            <v-list-tile-title > تجربه </v-list-tile-title>
                        </v-list-tile-content>

                    </v-list-tile>
                </v-list>
            </v-toolbar>
            <v-divider></v-divider>
            <v-list class="mb-4 mt-1 mr-2" centered>
                <v-list-tile v-for="view in views" :key="view.text" router :to="view.route" class="mt-2">
                    <v-list-tile-action>
                        <v-icon class="darkBlue--text">{{ view.icon }}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile> {{ view.text }}</v-list-tile>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
        <!-- </v-hover> -->
    </div>
</template>

<script>
    import {
        mapGetters
    } from 'vuex'

    export default {
        data() {
            return {
                mini: '',
                views: [{
                        icon: 'fas fa-flask',
                        text: 'التجارب',
                        route: '/'
                    },
                    {
                        icon: 'fas fa-feather',
                        text: ' كتابه تجربه',
                        route: '/editor'
                    },
                    {
                        icon: 'fas fa-user',
                        text: 'البروفايل',
                        route: '/profile'
                    },
                ]
            }
        },
        computed: {
            ...mapGetters(['sideNav']),
        },
        methods:{
            }
    }
</script>