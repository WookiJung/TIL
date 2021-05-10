<template>
  <div>
    <h2>Parent</h2>
    <input v-model="parentData" @input="onParentInput" type="text">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child 
      :appData="appData" :parentData="parentData"
      @childInput="onChildInput"
    />
  </div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  props:{
    appData: String
  },

  components:{
    Child,
  },
  data (){
    return {
      parentData: '',
      childData: '',
    }
  },
  methods:{
    onChildInput(childData) {
      this.childData = childData
      this.$emit('childInput', childData)
    },
    onParentInput() {
      this.$emit('parentInput', this.parentData)
    }
    
  }
}
</script>

<style scoped>

</style>

