n = int(input())

dic = {0:[1,0],1:[0,1]}

for _ in range(n):
    a,b = 0,0
    k = int(input())

    if k in dic : print(*dic[k])
    else:
        for i in range(len(dic),k+1):
            dic[i] = [dic[i-1][1], dic[i-1][1] + dic[i-1][0]]
        print(*dic[k])