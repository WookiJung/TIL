<template>
  <div>
    <h1>21.05.10 Workshop</h1>
    <input v-model="appData" type="text">
    <p>parentData: {{ parentData }}</p>
    <p>chidData: {{ childData }}</p>
    <!-- 3. 사용한다. -->
    <Parent :appData="appData" @child-input="onChildInput" @parent-input="onParentInput"/>
  </div>
</template>

<script>
// 1. 불러서
import Parent from '@/components/Parent.vue'

export default {
  name: 'Home',
  // 2. 등록하고
  components: {
    Parent,
  },
  data() {
    return {
      appData: '',
      childData: '',
      parentData: '',
    }
  },
  methods: {
    onChildInput(childData) {
      this.childData = childData
    },
    onParentInput(parentData) {
      this.parentData = parentData
    }
  },
}
</script>
