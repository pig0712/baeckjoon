import sys
input = sys.stdin.readline

a, b = map(int, input().split())

is_prime = [True] * (b + 1)

if b >= 0: is_prime[0] = False
if b >= 1: is_prime[1] = False


for i in range(2, int(b ** 0.5) + 1):
    if is_prime[i]:
        start = i**2
        step = i
        # i*i, i*i+i, i*i+2i, ... <= b 를 False로
        is_prime[start:b+1:step] = [False] * (((b - start) // step) + 1)
        # 4 : 17 : 2 = [False] * ()

# 출력 구간 보정(a가 2보다 작을 수 있음)
start = 2 if a < 2 else a

out = []
append = out.append
for x in range(start, b + 1):
    if is_prime[x]:
        append(str(x))

sys.stdout.write("\n".join(out))
