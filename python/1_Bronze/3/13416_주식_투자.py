test_case = int(input())

for _ in range(test_case):
    day = int(input())
    a = 0
    for _ in range(day):
        b = max(list(map(int,input().split())))
        if b > 0: a+=b
    
    print(a)