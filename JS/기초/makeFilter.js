// 기존의 filter 메서드
[1, 2, 3, 4, 5].filter(function (num) {
  return num % 2
})


// 직접 만드는 filter 함수
function filter(callback, arr) {
  const newArr = []

  for (const elem of arr) {
    if (callback(elem)) {  // callback 은 t/f 를 리턴하는 함수여야 한다.
      newArr.push(elem)
    }
  }
  
  return newArr
}


function isOdd (num) {
  return num % 2
}
filter(isOdd, [1, 2, 3, 4, 5])
