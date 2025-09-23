n = int(input())

for i in range(n):
    rep, s = input().split(" ")

    for j in s:
        print(j*int(rep), end="")
    print("")