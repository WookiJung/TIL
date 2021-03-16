from django.shortcuts import render
import random
import requests
from django.http.response import HttpResponse
# Create your views here.

# 사용자가 입력할 form & input용 html을 제공.
def ping(request):
    return render(request, 'practice0309/ping.html')


def pong(request):
    return render(request, 'practice0309/pong.html')



def var_route(request, string):

    return HttpResponse(string)


def lotto(request, value):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=' + str(value)
    result = requests.get(url).json()
    
    thistime = {result['drwtNo1'], result['drwtNo2'], result['drwtNo3'], result['drwtNo4'] , result['drwtNo5'], result['drwtNo6']}
    bonus = {result['bnusNo']}
    # jackpot = {f'{i}등' : 0 for _ in range(1,6)}
    No_1 = 0
    No_2 = 0
    No_3 = 0
    No_4 = 0
    No_5 = 0
    
    for _ in range(1000):
        lotto = random.sample(range(1,46),7)
        if len(set(lotto) & thistime) == 6:
            No_1 += 1
        if len(set(lotto) & thistime) == 5 and set(lotto) & bonus == bonus:
            No_2 += 1
        if len(set(lotto) & thistime) == 5:
            No_3 += 1
        if len(set(lotto) & thistime) == 4:
            No_4 += 1
        if len(set(lotto) & thistime) == 3:
            No_5 += 1
    nope = 1000 - (No_1+No_2+No_3+No_4+No_5)
    context = {
        'lotto': lotto,
        'No_1' : No_1,
        'No_2' : No_2,
        'No_3' : No_3,
        'No_4' : No_4,
        'No_5' : No_5,
        'thistime' : list(thistime),
        'bonus' : list(bonus)[0],
        'nope' : nope,
    }
    return render(request, 'practice0309/lotto_howmany.html', context)



        