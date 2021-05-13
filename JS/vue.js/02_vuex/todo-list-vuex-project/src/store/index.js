import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState()
  ],

  state: {
    todos:[
    
    ]
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      const idx = state.todos.indexOf(todoItem)
      state.todos.splice(idx, 1)
    },
    UPDATE_TODO(state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem){
          return {...todo, completed: !todo.completed }
        }
        return todo
      })
    }
  },
  actions: {
    createTodo({ commit }, todoItem){
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo({ commit }, todoItem){
      commit('DELETE_TODO', todoItem)
    },
    updateTodo({commit}, todoItem){
      commit("UPDATE_TODO", todoItem)
    }
  },
  getters:{
    completedTodosCount(state) {
      return state.todos.filter((todo) => {
        return todo.completed === true
      }).length
    },
    uncompletedTodosCount(state) {
      return state.todos.filter((todo) => {
        return todo.completed === false
      }).length
    },
  },
  modules: {
  }
})
