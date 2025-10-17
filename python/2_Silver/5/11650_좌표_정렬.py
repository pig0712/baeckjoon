import sys
input = sys.stdin.readline

n = int(input())

location = []
for i in range(n):
    location.append(list(map(int,input().split())))

for i in sorted(location):
    print(i[0],i[1])