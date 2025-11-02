n,k = list(map(int,input().split()))
lst = []
for i in range(1,n+1):
    if (int(str(i)[-1]) != int(str(k)[-1])) and (int(str(i)[-1]) != int(str(2*k)[-1])): lst.append(i)

print(len(lst))
print(*lst)