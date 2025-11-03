_ = input()

a = list(sorted(map(int,input().split())))

lst = [a[0]]

for i in range(1,len(a)):
    lst.append(lst[i-1] + a[i])

print(sum(lst))
