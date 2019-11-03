<template>
    <div class="pb-5 mb-5" id="scroll-target">
        <div class="postImg mb-4">
            <v-img :src="post.Img" alt="user" aspect-ratio="1.4" class="cover"></v-img>
            <div class="postCategory font-weight-bold mx-3">{{ post.Category }}</div>
        </div>
        <v-container px-3>
            <div class="postTitle text-xs-right my-4">
                <h1>{{ post.Title }}</h1>
            </div>
            <v-layout row align-center class="my-4">
                <v-flex shrink>
                    <v-avatar size="28" color="primary">
                        <img src="../../assets/img/avatar.png" alt="user">
                    </v-avatar>
                    <span class="gray--text font-weight-bold mx-2 body-1">زيد حسان</span>
                </v-flex>
                <v-spacer></v-spacer>
                <v-flex shrink>
                    <span>{{ post.Date }}</span>
                </v-flex>
            </v-layout>
            <div class="postContent text-xs-right my-4 body-1">
                <div id="postViewer" ref="postViewer"></div>
            </div>

            <comments-app />

            <v-bottom-nav color="white" :value="true" v-show="showNav" dark fixed class="mb-5">
                <v-btn dark fab icon small flat color="accent lighten-3">
                    <v-icon class="accent--text">fas fa-thumbs-up</v-icon>
                </v-btn>
                <v-btn dark fab icon small flat color="error lighten-3">
                    <v-icon class="error--text">fas fa-heart</v-icon>
                </v-btn>
                <v-btn dark fab icon small flat color="yellow lighten-3">
                    <v-icon class="yellow--text darken-1">fas fa-bookmark</v-icon>
                </v-btn>
            </v-bottom-nav>
        </v-container>

    </div>
</template>

<script>
    import {
        mapGetters
    } from 'vuex'
    import Quill from 'quill'
    import commentsApp from '@/components/Comments/comments.vue'

    export default {
        components: {
            commentsApp,
        },
        data() {
            return {
                offsetTop: 0,
                showNav: false,
            }
        },
        computed: {
            ...mapGetters(['delta', 'altejarub']),
            post() {
                const id = parseInt(this.$route.params.id);
                return this.altejarub.filter(function (tejrba) {
                    return tejrba.ID === id;
                })[0];
            },
        },

        mounted() {
            let article = this.$refs.postViewer
            let quill = new Quill(article, {
                readOnly: true
            })
            setTimeout(() => {
                quill.setContents(this.post.Delta)
            }, 0)
            // setTimeout(()=>{ this.$refs.postViewer.appendChild(article) },0)
        }
    }
</script>

<style lang="scss" scoped>
    @import '../../styles/views/singlePostPage/singlePostPage';
</style>