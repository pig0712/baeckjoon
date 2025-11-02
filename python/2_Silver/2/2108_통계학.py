import math
from sys import stdin
input = stdin.readline

def round_up(x):
    return math.floor(x + 0.5) if x >= 0 else math.ceil(x - 0.5)

data = []
for _ in range(int(input())):
    data.append(int(input()))
data = sorted(data)

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
if len(data) == 0: print(0)
else: print(round(sum(data)/len(data)))

# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값

if len(data) == 0: print(0)
elif len(data) % 2 == 0 : 
    print(data[round_up(len(data)/2)])
else: 
    print(data[round_up(len(data)/2)-1])

# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
""" 값별 개수 """
dic = {}
for i in data:
    if i in dic : dic[i] += 1
    else : dic[i] = 1

"""최빈값 저장"""
m = 0
storage = []
for i, j in dic.items():
    if m < j: m = j; storage = [i]
    elif m == j: storage.append(i)

"""최빈값 출력"""

if len(storage) == 1: print(storage[0])
else : print(storage[1])

# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
a,b = data[0], data[-1]
""" case 1 : a 가 양수, b가 양수 """
if (a >= 0) and (b >= 0):
    print(b-a)

    """ case 1 : a 가 양수, b가 음수 """ # 생각해보니 이런 경우는 이번 코드에는 없음
elif (a >= 0) and (b <= 0):
    pass

    """ case 1 : a 가 음수, b가 양수 """
elif (a <= 0) and (b >= 0):
    print(abs(a)+b)

    """ case 1 : a 가 음수, b가 음수 """
elif (a <= 0) and (b <= 0):
    print(abs(a) - abs(b))