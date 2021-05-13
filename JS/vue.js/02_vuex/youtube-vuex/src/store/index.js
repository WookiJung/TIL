import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    searchList : [],
    watchVideo: {},
    showDetail: false
  },
  mutations: {
    SEARCH_VIDEO(state, query) {
      state.searchList = []
      state.searchList.push(query)
    },
    WATCH_VIDEO(state, obj) {
      state.watchVideo = obj
      state.showDetail = true
    }
  },
  actions: { 
    searchVideo({ commit }, query) {
      commit('SEARCH_VIDEO', query)
    },
    watchVideo({commit}, obj){
      commit('WATCH_VIDEO', obj)
    }
  },
  modules: {
  }
})
