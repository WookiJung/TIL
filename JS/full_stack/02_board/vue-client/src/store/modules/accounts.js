// accounts.js
import axios from 'axios'
import DRF from '@/API/drf.js'
import router from '@/router'
import cookies from 'vue-cookies'

const state = {
  authToken: cookies.get('auth-token'),
}

const getters = {
  isLoggedIn : state => !!state.authToken,
  config: state => ({headers: {Authorization: `Token ${state.authToken}`}})
}

const mutations = {
  SET_TOKEN(state, token) {
    state.authToken = token
  }

}

const actions = {
  postAuthData({commit}, info){
    axios.post(DRF.URL + info.path, info.data)
      .then(res => {
        commit('SET_TOKEN', res.data.key)
        cookies.set('auth-token', res.data.key, '15MIN')
        //redirect to articles
        router.push({ name: 'List' })
      })
      .catch(err => {
        console.error(err.response.data)
      })
  },
  signup(context, signupData) {
    const info = {
      data: signupData,
      path: DRF.ROUTES.signup
    }
    context.dispatch('postAuthData', info)
  },
  login(context, loginData) {
    const info = {
      data: loginData,
      path: DRF.ROUTES.login
    }
    context.dispatch('postAuthData', info)

  },
  logout({getters, commit}) {
    const FULL_PATH = DRF.URL + DRF.ROUTES.logout
    axios.post(FULL_PATH, null, getters.config)
      .then(() => {
        cookies.remove('auth-token')  // 쿠키 삭제
        commit('SET_TOKEN', null) // state에서 삭제 
        router.push({ name:'List' })  // redirect
    })
      .catch(err => console.error(err))
  },

}

export default {
  state, getters, mutations, actions
}