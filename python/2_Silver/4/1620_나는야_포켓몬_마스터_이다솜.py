from sys import stdin
input = stdin.readline

n,m = map(int,input().split())

dic_num = {}
dic_name = {}

for i in range(1,n+1):
    a = input()
    dic_num[i] = a[:-1]
    dic_name[a[:-1]] = i

for _ in range(m):
    a = input()
    try :
        print(dic_num[int(a)])
    except:
        print(dic_name[a[:-1]])