# 입력
H,M = map(int,input().split(" "))
time = int(input())

# 입력받은 시간에 걸리는 시간 더해주기
M += time

# 분 처리
while M >= 60:

    if M >= 60:
        M -= 60
        H += 1
    else:
        break

# 시 처리
if H >= 24:
    H -= 24

# 출력
print(H,M)