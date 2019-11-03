import axios from 'axios'

// const localBaseUrl = 'http://localhost:8080/api/';
// const remoteBaseUrl = 'https://tejruba1.herokuapp.com/api'
// const CSRF_COOKIE_NAME = 'csrftoken';
// const CSRF_HEADER_NAME = 'X-CSRFToken';

let $backend = axios.create({
  baseURL: 'https://tajruba1.herokuapp.com/api',
  // timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    //   'Access-Control-Allow-Origin': '*'
  },
})

$backend.defaults.xsrfHeaderName = "X-CSRFToken"
$backend.defaults.xsrfCookieName = 'csrftoken'

// Response Interceptor to handle and log errors
$backend.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  return Promise.reject(error)
})

$backend.$register = (user) => {
  console.log(" user form backendjs "+ user +"user name: " + user.name +"  email: "+ user.email +" pass1: "+ user.password1 +" pass2: "+ user.password2)

  return $backend.post(`/accounts/register/`, {
      username: user.name,
      email: user.email,
      password: user.password1
    })
    .then(response => response.data)
}

export default $backend