import Vue from "vue";
import Vuex from "vuex";
import actions from './actions'
import mutations from './mutations'
import getters from './getters'
Vue.use(Vuex);

export default new Vuex.Store({
  state: {    // header 
    currentPage: '',
    experienceFilterValue:'',
    delta: undefined,
    content: '',
    FilterdExperiences: [],
    altjarub: [],
    comments:[],
    user:{
      ID:'',
      userName:'',
      userInfo:{}
    },
    userInfo:{},
    snackbar:{
      trigger : false,
      message : '',
      color: ''
    },

    sideNav:true
  },

  getters,
  mutations,
  actions,
});