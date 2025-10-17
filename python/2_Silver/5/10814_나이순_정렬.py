import sys
input = sys.stdin.readline

ages = {str(i):[] for i in range(1,201)}

n = int(input())

for _ in range(n):
    age, name = list(input().split())
    ages[age].append(name)

for i,j in enumerate(ages.values()):
    for k in j: 
        print(i+1,k)