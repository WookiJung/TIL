// articles.js
import axios from 'axios'
import DRF from '@/API/drf.js'
import router from '@/router'

const state = {
  articles: [],
}

const getters = {
  articles(state){
    return state.articles
  }

}

const mutations = {
  SET_ARTICLES(state, articles) {
    state.articles = articles
  }
}

const actions = {
  fetchArticles({ commit }) {
    axios.get(DRF.URL + DRF.ROUTES.articles)
      .then(res => {
        commit('SET_ARTICLES', res.data)})
      .catch(err => console.error(err))
  },
  createArticle(context, articleData) {
    axios.post(DRF.URL + DRF.ROUTES.articles, articleData, context.getters.config)
      .then(() => {
        router.push({ name:'List'})
      })
      .catch(err => console.error(err))
  }
}

export default {
  state, getters, mutations, actions
}