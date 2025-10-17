n = int(input())

player_score = {i : 0 for i in range(n)} # 플레이어 점수 저장

player_game = [[],[],[]]

for _ in range(n):
    a,b,c = list(map(int,input().split()))

    player_game[0].append(a)
    player_game[1].append(b)
    player_game[2].append(c)

for i in range(3):
    for j in range(len(player_game[i])):
        c = player_game.copy()
        if c[i][j] not in (c[i][:j] + c[i][j+1:]) : player_score[j] += c[i][j]

for i in range(n):
    print(player_score[i])