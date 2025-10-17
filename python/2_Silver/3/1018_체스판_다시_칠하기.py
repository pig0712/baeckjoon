n, m = list(map(int,input().split())) # 입력 받는 용도임

array = []

b = [
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"]
     ]

w = [
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"]
     ]

for i in range(n):
    array.append(list(input()))

counts = []

for i in range(n-7):
    for j in range(m-7):
        a = [row[j:j+8] for row in array[i:i+8]]

        count = 0
        for index_k, k in enumerate(b):
            for index_l, l in enumerate(k):
                if a[index_k][index_l] != b[index_k][index_l]: count += 1
        counts.append(count)

        count = 0
        for index_k, k in enumerate(w):
            for index_l, l in enumerate(k):
                if a[index_k][index_l] != w[index_k][index_l]: count += 1
        counts.append(count)


print(min(counts))