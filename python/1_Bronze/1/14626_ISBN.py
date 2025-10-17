n = input()

index = None
s = 0
for i,j in enumerate(n[:12]):
    if j != "*":
        if i % 2 == 0: s += int(j)
        else : s += int(j) * 3
    else: index = i



# # 그냥 0 ~ 9 까지 다 넣어보고 계산 때려버리기
for i in range(10):
    if index % 2 == 0: 
        if (10 - (s + i)) % 10 == int(n[-1]):
            print(i)
            break
    else:
        if (10 - (s + (i * 3))) % 10 == int(n[-1]):
            print(i)
            break