<template>
  <div>
    <h2>Parent</h2>
    <input v-model="parentData" @input="onParentInput">
    <p>appData: {{ appData }}</p>
    <p>chidData: {{ childData }}</p>
    <Child 
      :appData="appData" :parentData="parentData" 
      @child-input="onChildInput"
    />
  </div>
</template>

<script>
import Child from './Child.vue'

export default {
  name: 'Parent',
  components: {
   Child
  },
  props: {
    appData: String,
  },
  data () {
    return {
      parentData: '',
      childData: '',
    }
  },
  methods: {
    onChildInput(childData) {  // 아래에서 발생한 event => 데이터가 함께 오기에 인자 필요
      this.childData = childData
      this.$emit('child-input', childData)
    },

    onParentInput() {  // 여기서 발생한 event => 위로 올리기만 하면 되기에 인자 X
      this.$emit('parent-input', this.parentData)
    }
  }

}
</script>

<style>

</style>