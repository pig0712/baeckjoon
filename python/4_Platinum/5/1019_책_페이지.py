import sys
input = sys.stdin.readline

N = int(input().strip())
cnt = [0] * 10

p = 1
while p <= N:
    high = N // (p * 10)
    cur  = (N // p) % 10
    low  = N % p

    for d in range(10):
        cnt[d] += high * p # 완전하게 반복된 세트 수 × 세트 내 등장 횟수(p)

    for d in range(cur): # 미완성 세트 수 계산 
        cnt[d] += p
    cnt[cur] += low + 1 # 마지막 자기 자신 

    cnt[0] -= p # 0 보정
    p *= 10 # 자리수 변환

print(*cnt)
