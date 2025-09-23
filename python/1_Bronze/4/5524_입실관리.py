n = int(input())

lst = []
for i in range(n):
    lst.append(str(input()).lower())

for i in range(n):
    print(f"{lst[i]}")