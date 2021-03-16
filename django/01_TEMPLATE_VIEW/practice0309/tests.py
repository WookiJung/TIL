from django.test import TestCase


def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    requests.get(url)

lotto(request)
# Create your tests here.
