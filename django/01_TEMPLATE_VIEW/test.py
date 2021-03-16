import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
r = requests.get(url)
set_r = {r.text['drwtNo5']}

print(r.text)
print(set_r)