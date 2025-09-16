count = [1,1,2,2,2,8]
nums = list(map(int,input().split()))
re = [j-nums[i] for i,j in enumerate(count)]

for i in re[:-1]:
    print(i,end=" ")
print(re[-1])