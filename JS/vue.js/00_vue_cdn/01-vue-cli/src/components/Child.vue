<template>
  <div>
    <h2>Child</h2>
    <input v-model="childData" @input="onInputChange" type="text">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props:{
    appData: String,
    parentData: String,
  },
  data() {
    return{
      childData: '',
    }
  },
  methods: {
    onInputChange() {
      
      this.$emit('childInput', this.childData)

    }
  }

}
</script>

<style scoped>

</style>>

