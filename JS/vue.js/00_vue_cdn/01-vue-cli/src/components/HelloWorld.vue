<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <p>menu</p>
      <li>{{lunch}}</li>
      <li>{{dinner}}</li>
    </ul>
    <h3>{{ todayMenu }}</h3>
      
    <h3>wow</h3>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {  // 자세한 정보는 vue.JS 스타일가이드 참조.
    msg: String,
    lunch: String,
    dinner: String,
  },
  computed:{
    todayMenu() {
      return `오늘 점심은 ${this.lunch}, 오늘 저녁은 ${this.dinner}`
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
  color: red;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
