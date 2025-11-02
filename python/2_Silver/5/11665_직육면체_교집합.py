from sys import stdin
input = stdin.readline

n = int(input())

# x,y,z 좌표의 범위를 구해 저장후 다음 입력값에 겹치는 부위 x1 * y1 * z1 해서 구하기
coordinates = [[] for i in range(6)] # x1,y1,z1,x2,y2,z2

# 입력 받기
for _ in range(n):
    for i,j in enumerate(map(int,input().split())):
        coordinates[i].append(j)

# 좌표 교집합 범위 추출후 출력
x = max(0 ,min(coordinates[3]) - max(coordinates[0]))
y = max(0 ,min(coordinates[4]) - max(coordinates[1]))
z = max(0 ,min(coordinates[5]) - max(coordinates[2]))
print(x*y*z)