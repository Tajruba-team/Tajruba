//getters
export default {
        delta: state => state.delta,
        contents: state => state.content,
        textContent: state => {
                var tag = document.createElement('div')
                tag.innerHTML = state.content
                return tag.innerText
        },
        altejarub: state => state.altjarub,
        comments: state => state.comments,
        userInfo: state => state.userInfo,
        snackbar: state => state.snackbar,
        sideNav: state => state.sideNav,
}