<template>
  <v-container class="pa-2">
    <!-- toolbar -->
    <v-layout row justify-center align-center wrap class="mt-3">
      <v-btn @click="uploadDialog = true" color="white" class="primary--text">
        <v-icon small right class="ml-2">fas fa-image</v-icon>
        <span> صوره </span>
      </v-btn>

      <!-- dialog -->
      <v-dialog v-model="uploadDialog" max-width="500px">
        <v-card>
          <v-card-title>
            إختيار صوره
          </v-card-title>
          <v-divider></v-divider>
          <v-img
            v-if="ImgUrl"
            contain
            height="auto"
            :src="ImgUrl"
          >
            
          </v-img>
          <v-card-text>
            <v-layout column wrap align-start>
              <v-flex shrink>
                <v-btn @click="onPickImg" class="mb-3">
                  <v-icon small right @click="uploadDialog = true" class="primary--text">fas fa-upload</v-icon>
                  <span> إختيار صوره من الجهاز </span>
                </v-btn>
                <input v-show="false" type="file" ref="imgInput" accept="image/*" @change="onImgUploaded">
              </v-flex>
              <v-divider class="mx-4" dark></v-divider>
              <v-flex>
                <v-text-field solo append-icon="fas fa-link" label="عنوان الصوره" placeholder="لصق رابط الصوره"
                  v-model="ImgUrl"></v-text-field>
              </v-flex>
            </v-layout>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn class="ml-3" :class="[isDisabled ? '' : 'publish']" color="success" text @click="onSaveUploadedImg" :disabled='isDisabled'>
              حفظ
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="white darken-1" @click="onCancelImgUpload">
              <v-icon small right color="error">fas fa-trash</v-icon>
              <span>الغاء</span>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <!-- dialog -->
      <v-btn router to="/signup">
        <v-icon small right class="primary--text ml-2">fas fa-search</v-icon>
        <span>unsplash</span>
      </v-btn>
      <v-spacer></v-spacer>
    </v-layout>

    <v-form ref="editorForm" v-model="valid" lazy-validation>
      <v-text-field 
      class="primary--text mt-3" 
      color="primary" 
      outline
      background-color="#eee"
      v-model="Title"
      name="name" 
      label="عنوان التجربه" 
      :rules="[v => !!v || 'قم بإدخال عنوان للتجربه']" required >
      </v-text-field>

      <v-select 
      class="primary--text" 
      outline
      background-color="#eee"
      :items="categories" 
      :rules="[v => !!v || 'يجب إختيار فئه للتجربه']" v-model="Category"
      label="إختر فئه التجربه" chips  clearable required>
      </v-select>

      <!-- editor -->
      <quill-editor calss="text-justify" v-model="content" id="editorQuill" ref="myTextEditor" :options="editorOption">
      </quill-editor>
    <v-text-field
      ref="valditionFieldForEditor"
      type="hidden"
      class="hiddenInput"
      :rules="editorRules"
      required
      background-color="transparent" color="transparent"
      :value="validationText"
    ></v-text-field>
    </v-form> 
    
    <!-- control -->
    <v-layout row wrap class="mb-5">
      <v-btn @click="test()"> حفظ </v-btn>
      <v-spacer></v-spacer>
      <v-btn class="publish elevation-15" @click="publish()" dark> نشر </v-btn>
    </v-layout>
            <snack-bar/>
  </v-container>
</template>


<script>
  import 'quill/dist/quill.bubble.css'
  // import 'quill/dist/quill.snow.css'
  import {
    quillEditor
  } from 'vue-quill-editor'
  import {
    mapGetters
  } from 'vuex'
  import moment from 'moment'
  import snackBar from '@/components/sharedComponents/snackbar.vue'
  export default {
    components: {
      quillEditor,
      snackBar
    },
    data() {
      return {
        content: '',
        isMounted: false,
        uploadDialog: false,
        image:null,

        ID: '',
        ImgUrl: null,
        Title: '',
        Category: '',
        Delta: '',
        content: '',
        satus: '',
        Hearts: '',
        Likes: '',
        Stars: '',

        valid:true,
        snackBar_error:false,
        editorRules:[
          v => !!v || 'قم بكتابه تجربتك',
          v => (v && v.length >= 800) || 'طول التجربه على الاقل 800 حرف'
        ],
        categories: [
          'رياضه',
          'فن',
          'صحه',
          'تعليم',
          'مهارات حياه',
          'تصميم',
          'ترفيه',
          'برمجه'
        ],


        editorOption: {
          theme: 'bubble',
          placeholder: "إبدا بكتابه تجربتك...",
          modules: {
            toolbar: [
              ['bold', 'italic', 'underline', 'strike'],
              [{
                'list': 'ordered'
              }, {
                'list': 'bullet'
              }],
              [{
                'header': [1, 2, 3, 4, false]
              }],
              [{
                'color': []
              }, {
                'background': []
              }],
              [{
                'font': []
              }],
              [{
                'align': []
              }],
              ['link', 'image'],
            ]
          },
        },
      }
    },
    mounted: function () {
      this.$refs.myTextEditor.quill.format('align','right')
        this.$refs.myTextEditor.quill.format('direction', 'rtl')
      this.isMounted = true
      this.$store.state.currentPage = this.$route.name;

      if (!this.content && this.contents) {
        this.content = this.contents
      }
    },

    watch: {
      content(val) {
        if (!this.isMounted) {
          this.$store.commit('setDelta', this.$refs.myTextEditor.quill.getContents())
        }
        this.$store.commit('setContent', val)
        this.isMounted = false
      },
    },

    computed: {
      ...mapGetters(['delta', 'contents','textContent','snackbar']),
      validationText(){
        return this.textContent
      },
      isDisabled(){
        if(!this.ImgUrl){
          return true
        }
        return false
      }
    },
    methods: {
      publish: function () {
          if(this.$refs.editorForm.validate()){
          this.$store.commit('publishPost', {
            ID: this.$store.state.altjarub.length,
            Img: this.ImgUrl,
            Title: this.Title,
            Category: this.Category,
            //--
            Delta: this.delta,
            content: this.textContent,
            //--
            Date: this.$moment().fromNow(),
            //--
            Hearts: this.Hearts,
            Stars: this.Stars,
            Likes: this.Likes,
          });
          this.$router.replace(`/postPage/${this.$store.state.altjarub.length-1}`);
          this.$refs.editorForm.reset();
          this.$refs.myTextEditor.quill.setContents([{ insert: '\n' }]);
        } else {
          let snackbar = {
            message: 'أعد التحقق من البيانات المدخله',
            color: 'error'
          }
          this.$store.commit('updateSnackbar', snackbar)
        }
      },
      onSaveUploadedImg: function () {
        this.uploadDialog = false
      },
      onCancelImgUpload: function () {
        this.ImgUrl = null
        this.uploadDialog = false
        this.image = null
      },
      onPickImg: function() {
        this.$refs.imgInput.click()
      },

      onImgUploaded: function(event) { 
        const file = event.target.files[0]
        let fileName = file.name
        this.image = file
        const allowedType = ['image/jpeg', 'image/png', 'image/gif']
        const isAllowedType = allowedType.includes(file.type)   
        if(fileName.lastIndexOf('.') <= 0){
          return alert('قم باضافه صوره صالحه')
        }
        const fileReader = new FileReader()
        fileReader.addEventListener('load',()=>{
          this.ImgUrl = fileReader.result
        })
        fileReader.readAsDataURL(file)
      }
    },
  }
</script>

<style lang="scss">
  @import '../../styles/views/editor';
</style>