n = int(input())

c = 0
for _ in range(n):

    a = input()

    j = -1
    for i in range(len(a)):
        if ((a[i+1:].find(a[i])) == 0) or ((a[i+1:].find(a[i])) == -1):
            j = 1
            continue
        else:
            j = 0
            break



    c += j

print(c)