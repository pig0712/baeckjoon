import sys
n = int(input())

for i in range(n):
    a,b = map(int,sys.stdin.readline().split(' '))
    print(a+b)


# sys.stdin.readline() 이 함수에 대해 더 알아보기