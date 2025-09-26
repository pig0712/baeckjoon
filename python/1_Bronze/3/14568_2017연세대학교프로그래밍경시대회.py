n = int(input())

count = 0

for c in range(2,n+1,2):
    for b in range(1,n-c+1):
        if n-(c+b) == 0: continue
        if (n-(c+b)) - b >= 2:
            count += 1

print(count)


"""
1< N < 100

남는 사탕은 없어야 한다.

남규는 영훈이보다 2개 이상 많은 사탕을 가져야 한다.

셋 중 사탕을 0개 받는 사람은 없어야 한다. 0 

택희가 받는 사탕의 수는 홀수개가 되어서는 안 된다. 0
"""