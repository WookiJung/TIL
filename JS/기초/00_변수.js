/*
camelCase === lowerCamelCase
변수, 상수, 함수명

PascalCase === UpperCamelCase
class 명

UPPER_SNAKE_CASE
절대 변하면 안되는 상수 값
*/

// let => 변수, 재할당 가능
let x = 1
x = 2

// const => 상수, *재할당* 불가능
const y = 1
y = 2  // ERROR


// Scope
// 블록 ({ block }) 스코프

const greeting = 'hello'

if (true) {
  console.log(greeting)
  let y = 1
}
console.log(y)  // Error
 
