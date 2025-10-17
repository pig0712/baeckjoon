n,m = list(map(int,input().split())) # n 사용 x
a = sorted(list(map(int,input().split())))

best_num = [-1,99999999999999999]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            aa = a[i]+a[j]+a[k]
            if aa > m : continue
            if aa == m : print(aa); exit()
            else:
                if best_num[1] > m-aa: best_num[0] = aa; best_num[1] = m-aa

print(best_num[0])