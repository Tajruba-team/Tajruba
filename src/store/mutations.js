//mutations
export default {
    setDelta(state, payload) {
      state.delta = payload;
    },

    setContent(state, payload) {
      state.content = payload;
    },
    
    publishPost(state, payload){
      state.altjarub.push({...payload});
    },

    updateSnackbar(state, payload) {
      state.snackbar.trigger = true
      state.snackbar.message = payload.message
      state.snackbar.color = payload.color
    },

    addComment(state,payload){
      state.comments.unshift(payload)
    },
    
    UpdateUserInfo(state, payload){
      state.userInfo = payload
    },
    UpdateUserAvatar(state, payload){
      state.userInfo = payload
    },
    ToggleSideNav(state){
      state.sideNav = !state.sideNav
    },

}