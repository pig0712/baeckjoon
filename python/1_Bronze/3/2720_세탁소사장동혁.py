lst = [25,10,5,1]

a = int(input())

result = []
for i in range(a):
    ip = int(input())
    count = count = [0,0,0,0]
    for j in range(len(count)) :
        count[j] = ip // lst[j]
        ip %= lst[j]
    result.append(count)

for i in result:
    for j in i:
        print(j,end=" ")
    print("")