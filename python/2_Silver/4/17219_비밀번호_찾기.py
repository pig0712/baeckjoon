from sys import stdin
input = stdin.readline

n,m = map(int,input().split())

url = {}
password = {}

for _ in range(1,n+1):
    a = input().split()
    url[a[0]] = a[1]

for _ in range(m):
    a = input()[:-1]
    print(url[a])