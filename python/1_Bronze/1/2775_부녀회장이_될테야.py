test_case = int(input())
for i in range(test_case):
    k,n = int(input()), int(input())
    lst = [None]
    lst[0] = [i for i in range(1,n+1)]
    try : 
        print(lst[k][n-1])
    except IndexError:
        for ii in range(1,k+1):
            for j in range(1,n+1):
                if j == 1 : lst.append([1]); continue
                lst[ii].append(lst[ii][j-2]+lst[ii-1][j-1])
                print(lst)
        print(lst[k][n-1])