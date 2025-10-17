from sys import stdin

input = stdin.readline

_ = input()

x = list(map(int,input().split()))

_ = input()

y = list(map(int,input().split()))

dic = {}
for i in x:
    try:
        dic[i] += 1
    except:
        dic[i] = 1

for i in y:
    try:
        print(dic[i])
    except:
        print("0")