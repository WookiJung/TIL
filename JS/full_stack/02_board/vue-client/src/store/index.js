import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import artilces from './modules/articles'
import errors from './modules/errors'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, artilces, errors }
})
