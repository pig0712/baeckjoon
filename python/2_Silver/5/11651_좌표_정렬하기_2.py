import sys
input = sys.stdin.readline

n = int(input())

location = []
for i in range(n):
    a = list(map(int,input().split()))
    a.reverse()
    location.append(a)
    
for i in sorted(location):
    print(i[1],i[0])