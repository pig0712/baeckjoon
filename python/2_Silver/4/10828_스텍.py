from collections import deque
from sys import stdin

input = stdin.readline
stack = deque()
n = int(input())

for _ in range(n):
    st = input()
    if st.find("push") != -1: stack.appendleft(int(st.replace("push ","")))
    elif st.find("pop") != -1:
        if len(stack) == 0: print(-1)
        else: print(stack.popleft()) 
    elif st.find("size")!= -1: print(len(stack))
    elif st.find("empty") != -1:
        if len(stack) == 0: print(1)
        else: print(0)
    else:
        if len(stack) == 0: print(-1)
        else: print(stack[0])