_ = int(input())

lst = list(map(float,input().split(' ')))

lst1 = []
for n,i in enumerate(lst):
    lst1.append(i/max(lst)*100)

print(sum(lst1)/len(lst1))