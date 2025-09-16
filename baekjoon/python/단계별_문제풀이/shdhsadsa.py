import numpy as np

# 비용표 {C_i_j} ( 5x5 행렬 )
cost = np.array([[3, 7, 8, 6, 5],
                 [4, 8, 10, 6, 6],
                 [5, 7, 9, 6, 7],
                 [4, 7, 10, 6, 8],
                 [6, 9, 11, 10, 9]])


# 행별 최소 비용 {p_i}

p = []
for i in range(len(cost)):
    p.append(cost[i].min())
p = np.array(p)
p = np.reshape(p,(5,1))

print(f"행별 최소비용:\n\n{p}\n\n")

# 기회비용표 {C_i_j - p_i}
cost = cost - p
print(f"기회비용표: \n\n{cost}\n\n")

# 열별 최소 비용 {q_i}

q = []
for i in range(len(cost[0])): # 행마다 다 같은 열을 개수를 가지고 있으니 cost[0] 으로 지정함
    print(i)