<template>
  <div>
    <h1>05.10 workshop</h1>
    <h2>App</h2>
    <input v-model="appData" type="text">
    <p>parentData: {{parentData}}</p>
    <p>childData: {{childData}}</p>
    <Parent :appData='appData' 
    @parentInput="onParentInput" @childInput="onChildInput"
    />
  </div>
  <!-- 3.사용한다. -->
</template>

<script>
import Parent from './components/Parent.vue'
// 1. 불러서
const obj = {
  name: "App",
  // 등록하고
  components: {
    Parent,
  },
  data() {
    return {
      appData: '',
      parentData: '',
      childData:'',
    }
  },
  methods: {
    onParentInput(parentData) {
      this.parentData = parentData
    },
    onChildInput(childData) {
      this.childData = childData
    }

  }
  
}

export default obj
</script>

<style scoped>

</style>