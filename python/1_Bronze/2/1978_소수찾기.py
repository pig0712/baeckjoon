_ = input()

a = sorted(list(map(int,input().split())))

# 소수 계산
b = [2]
for i in range(3,1001):
    t = False
    for j in b:
        if i % j == 0 : t = True; break

    if t == False:
        b.append(i)

c = 0
for i in a:
    if i in b: c += 1
print(c)