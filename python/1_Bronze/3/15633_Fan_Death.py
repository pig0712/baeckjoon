n = int(input())
lst = []

for i in range(1,round(n**(1/2))+1):
    if n % i == 0:
        lst.append(i)
        lst.append(int(n/i))

lst = sum(set(sorted(lst)))

print((lst * 5) -24)
    
# 약수 ㅈㄴ 빠르게 구하는 알고리즘 있었는데 그거 공부해서 하기