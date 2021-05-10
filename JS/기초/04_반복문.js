let i = 0
while (i < 5) {
  console.log('hi')
  i++
}


const numbers = [1, 2, 3, 4, 5]
// 전통적인 for
for (let j=0; j<arr.length; j++) {
  console.log(arr[j])
}

// Array용 => 요소를 꺼내는 for - of
for (const number of numbers) {
  console.log(number)
}

// Object => Key 를 꺼내는 for - in
const person = {name: 'neo', 'address': 'seoul'}
for (const key in person) {
  console.log(key, person[key])
}