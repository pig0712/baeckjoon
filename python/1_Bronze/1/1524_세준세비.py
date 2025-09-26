T = int(input()) # test case 수


for i in range(T): # test case 만큼 반복
    "입력"
    # 세준
    _ = input()
    _ = input()
    N = max(list(map(int,input().split())))
    # S = {i : N.count(i) for i in set(N)} # 딕셔너리 컴프리핸션으로 최소화

    # 세비
    M = max(list(map(int,input().split())))
    # B = {i : M.count(i) for i in set(M)} # 딕셔너리 컴프리핸션으로 최소화
    
    "연산"
    
    if N > M:
        print("S")
    elif N < M:
        print("B")
    else:
        print("S")

# 시간 초과
# for i in range(T): # test case 만큼 반복
#     "입력"
#     # 세준
#     _ = input()
#     _ = input()
#     N = sorted(list(map(int,input().split())))
#     S = {i : N.count(i) for i in set(N)} # 딕셔너리 컴프리핸션으로 최소화

#     # 세비
#     M = sorted(list(map(int,input().split())))
#     B = {i : M.count(i) for i in set(M)} # 딕셔너리 컴프리핸션으로 최소화
    
#     "연산"
    
#     if max(S.keys()) > max(B.keys()):
#         print("S")
#     elif max(S.keys()) < max(B.keys()):
#         print("B")
#     elif max(S.keys()) == max(B.keys()):
#         print("S")






    # 시간 초과
    # while len(S) != 0 or len(B) != 0:
    #     try:
    #         # 힘 부터 연산 #

    #         # 세준 > 세비
    #         if min(S.keys()) > min(B.keys()): # 힘 자체가 딸릴때
    #             del B[min(B.keys())]

    #         # 세준 < 세비
    #         elif min(S.keys()) < min(B.keys()): # 힘 자체가 딸릴때
    #             del S[min(S.keys())]

    #         # 세준 = 세비
    #         elif min(S.keys()) == min(B.keys()):
    #             del B[min(B.keys())]

    #     except ValueError:
    #         break
    
    # if len(S) == 0: print("B")
    # elif len(B) == 0: print("S")