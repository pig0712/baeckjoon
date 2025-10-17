# # 1
# import math
# n = list(map(int,input().split()))

# print(math.gcd(n[0],n[1]))
# print(math.lcm(n[0],n[1]))


# 2 : 함수 직접 구현

# 최대 공약수 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소 공배수 구하기
def lcm(a,b):
    return int(a*b / gcd(a,b))

a,b = list(map(int,input().split()))

print(gcd(a,b))
print(lcm(a,b))