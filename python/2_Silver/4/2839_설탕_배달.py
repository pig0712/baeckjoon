n = int(input())

sugar = 9999999


for i in range(int(n // 5) + 1):
    for j in range(int(n // 3) + 1):
        if (i*5) + (j*3) == n: 
            if sugar > i + j:
                sugar = i + j

if sugar == 9999999:
    print(-1)
else:
    print(sugar)