<template>
  <div id="app">
    <h1>Todo App</h1>
    <p>Completed : {{ completedTodosCount }}</p>
    <p>Uncompleted : {{ uncompletedTodosCount }}</p>
    <TodoForm />
    <TodoList />
    
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed: {
    // completedTodosCount() {
    //   return this.$store.getters.completedTodosCount
    // },
    // uncompletedTodosCount() {
    //   return this.$store.getters.uncompletedTodosCount
    // },
    ...mapGetters([
      'completedTodosCount', 'uncompletedTodosCount'
    ])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
