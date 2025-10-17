# from sys import stdin
# input = stdin.readline

# array = []
# for _ in range(int(input())):
#     array.append(input().replace("\n",""))

# array = list(set(array)) # 중복 제거

# array_len = [None for _ in range(len(array))]

# for i,j in enumerate(array):
#     array_len[i] = len(j)

# dic = {i: [] for i in range(1,51)}

# # 문자 수 별로 정렬.
# for i,j in enumerate(array_len):
#     dic[j].append(i)

# result = []
# # 문자 사전 순으로 변경
# for i in dic.values():
#     # 다시 문자로 변환
#     for j,k in enumerate(i):
#         i[j] = array[k]
#     i = sorted(i)
    
#     for l in i:
#         result.append(l)

# for i in result:
#     print(i)


#### 위 코드를 ㅈㄴ 간단하게 푼사람이 있음 ####
import sys
n = int(sys.stdin.readline())
words = list(set([sys.stdin.readline().strip() for _ in range(n)]))
words.sort()
print('\n'.join(sorted(words, key=len)))