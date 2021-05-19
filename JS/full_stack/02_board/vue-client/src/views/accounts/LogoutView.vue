<template>
  <div>
    이모든작업은 vue-router기준 URL을 구성하기 위함이다.
    왜냐하면 URL:Component는 1:1을 구성하니까.
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name:'LogoutView',
  methods:{
    ...mapActions(['logout'])
  },
  created() {
    this.logout()
  }
}
</script>

<style>

</style>