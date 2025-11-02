from collections import deque

for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    im = deque(list(map(int,input().split())))
    # [1,2,3,4] # 중요도

    n = deque([i for i in range(n)])
    # [0,1,2,3] # 문서

    c = 0
    a = len(im)
    cc = False
    while len(im) != 0:
        for i in range(a):
            if (im[0] == max(im)) and (n[0] == m): c += 1;  cc = True ;break 
            if im[0] == max(im): c += 1; n.popleft(); im.popleft();
            else: n.append(n.popleft()); im.append(im.popleft())
        if (cc == False) and (im[0] == max(im)) and (n[0] == m): c += 1;  break
        elif (im[0] == max(im)) and (n[0] == m): break
    print(c)