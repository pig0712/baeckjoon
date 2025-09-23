n = int(input()) # 시험장 개수 (사용 안할듯 이 변수는)

a = list(map(int,input().split())) # i번 시험장의 응시자수
b,c = list(map(int,input().split())) # 총감이 한번에 응시 가능수 b, 부감이 한번에 응시 가능수 c

d = 0
for i in a:
    if i >= b:
        i -= b
        d += 1

        while i > 0:
            i -= c
            d += 1

print(d)