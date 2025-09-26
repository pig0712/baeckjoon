t = int(input())
for _ in range(t):
    h,w,n = list(map(int,input().split())) # 층수, 호실수, n번째 손님
    print(f"{(n-1)%h+1}{(n-1)//h+1:02d}")