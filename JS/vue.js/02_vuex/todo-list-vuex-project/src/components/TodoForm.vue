<template>
  <div>
    <input type="text" v-model="todoTitle" @keyup.enter="createTodo">
    <button @click="createTodo">생성하기</button>
  </div>
</template>

<script>
export default {
  name:'TodoForm',
  data() {
    return {
      todoTitle: '',
    }
  },
  methods: {
    createTodo() {
      const todoItem = {
        title: this.todoTitle,
        completed:false,
      }
      if (todoItem.title.trim()) {
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = ''
    }
  }

}
</script>

<style>

</style>