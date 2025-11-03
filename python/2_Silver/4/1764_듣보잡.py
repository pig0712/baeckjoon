from sys import stdin
input = stdin.readline

n = sum(map(int,input().split()))

dic = {}

for _ in range(n):
    a = input()[:-1]

    if a in dic : dic[a] += 1
    else : dic[a] = 1

c = 0
lst = []
for i, j in dic.items():
    if j == 2 : c+=1; lst.append(i)

print(c)
print(*sorted(lst), sep="\n")