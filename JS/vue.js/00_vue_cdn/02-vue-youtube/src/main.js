import Vue from 'vue'  
// 폴더위치 명시가 없으면 => 1. 내위치 2. node modules 탐색.
import App from './App.vue'
// 위치명시 => 위치에서 찾기.

new Vue({
  render: h => h(App)
}).$mount('#app')
// or 마지막에 .$mount('#app')을 쓰면 el:'#app'을 대체가능.
// mainJS에서 #app의 id는 index.html에서 id=app을 잡는거야.