from collections import deque

n, k = list(map(int,input().split()))

peoples = deque([i for i in range(1,n+1)])
result = []
while len(peoples) != 0:

    for _ in range(k-1):
        peoples.append(peoples.popleft())
    result.append(peoples.popleft())

print(str(result).replace("[","<").replace("]",">"))