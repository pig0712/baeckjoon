lst = [i for i in range(1,31)]

for _ in range(28):
    a = int(input())
    lst.remove(a)

for i in lst:
    print(i)