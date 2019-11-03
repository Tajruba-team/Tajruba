import $backend from '@/backend';
export default {
  register(state ,user) {
    console.log("user from action " + user + user.name)

    return new Promise((resolve, reject) => {
    
      $backend.$register(user).then(responseDate => {
        console.log( "responseDate -- == " + responseDate)
          resolve(responseDate)
        })
        .catch(err => {
          reject(err)
        })
    })
  },
}