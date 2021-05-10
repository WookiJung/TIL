const id = 'admin'

if (id === 'admin') {
  console.log('관리자님, 환영합니다.')
} else if (id === 'manager') {
  console.log('매니저님 환영합니다.')
} else {
  console.log(`${id} 님, 환영합니다`)
}


switch (id) {
  case 'admin': {
    console.log('관리자님, 환영합니다.')
    break
  }
  case 'manager': {
    console.log('매니저님 환영합니다.')
    break
  }
  default: {
    console.log(`${id} 님, 환영합니다`)
  }
}
