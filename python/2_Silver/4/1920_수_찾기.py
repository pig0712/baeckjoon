# 이분 탐색 알고리즘 사용
import sys

def Binary_Search(x,target,start, end):
    if (start > end):
        return False

    mid = (start + end) // 2

    if target == x[mid]: return True # 중앙 값이 타겟 값과 같으면 반환
    elif target > x[mid]: return Binary_Search(x,target,mid+1,end) # 중앙 값이 타겟 값보다 작으면 오른쪽 중앙 값 기준 오른쪽 값들만 가져와 다시 판단
    else: return Binary_Search(x,target,start,mid-1) # 위의 라인과 반대 상황

input = sys.stdin.readline
print = sys.stdout.writelines
_ = input()

x = sorted(list(map(int,input().split())))

_ = input()

y = list(map(int,input().split()))

for target in y:
    print(str(int(Binary_Search(x,target,0,len(x)-1)))+"\n")

"""------------------------------------------------------------------------------------------"""
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# _ = input()

# x = list(map(int,input().split()))

# _ = input()

# y = list(map(int,input().split()))

# for i in y:
#     try:
#         a = x.index(i)
#         print("1"+"\n")
#     except:
#         print("0"+"\n")
"""시간 초과 -> 이분 탐색 알고리즘으로 해보기"""
