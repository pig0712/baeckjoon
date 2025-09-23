a, b = list(map(int,input().split()))

m_A = []
m_B = []

for i in range(a):
    m_A.append(list(map(int,input().split())))

for i in range(a):
    m_B.append(list(map(int,input().split())))

for i in range(a):
    for j in range(b):
        m_A[i][j] += m_B[i][j]

for i in range(a):
    for j in range(b):
        print(m_A[i][j],end=" ")
    print("")