from collections import deque

# 입력
N, M = map(int, input().split())
m = [list(map(int, input().strip())) for _ in range(N)]

# 이동 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위를 벗어나거나 이동할 수 없는 칸이면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M or m[nx][ny] == 0:
                continue

            # 처음 방문하는 칸에 대해서만 처리
            if m[nx][ny] == 1:
                m[nx][ny] = m[x][y] + 1
                queue.append((nx, ny))

    # 도착점의 거리 반환
    return m[N-1][M-1]

# 결과 출력
print(bfs(0, 0))