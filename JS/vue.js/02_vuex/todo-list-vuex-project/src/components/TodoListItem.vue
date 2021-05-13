<template>
  <div>
    <span 
    @click="updateTodo(todo)"
    :class="{ completed: todo.completed }"
    >{{ todo.title }}</span>
    <button @click="deleteTodo">Delete</button>

  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'TodoListItem',
  props:{
    todo: Object,
  },
  methods: 
  {...mapActions(['updateTodo', 'deleteTodo'])}
  // { deleteTodo() {
  //     this.$store.dispatch('deleteTodo', this.todo)
  //   },
  //   updateTodo() {
  //     this.$store.dispatch('updateTodo', this.todo)
  //   }
  // } 
  //이 코드를 위와같이 축약가능.
}
</script>

<style scoped>
  .completed {
    text-decoration: line-through;
  }
</style>