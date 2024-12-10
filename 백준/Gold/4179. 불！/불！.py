from sys import stdin
from collections import deque

R, C = map(int, stdin.readline().split())
board = []
fire = []
jh = []
for _ in range(R):
    row = stdin.readline().strip()
    board.append(row)
    fire.append([-1] * C)
    jh.append([-1] * C)

queue_j = deque()
queue_f = deque()
for x in range(R):
    for y in range(C):
        if board[x][y] == "J":
            jh[x][y] = 0
            queue_j.append([x, y])
        if board[x][y] == "F":
            fire[x][y] = 0
            queue_f.append([x, y])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 불 bfs
while queue_f:
    cx, cy = queue_f.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if board[nx][ny] == "#" or fire[nx][ny] >= 0:
            continue
        fire[nx][ny] = fire[cx][cy] + 1
        queue_f.append([nx, ny])

# 지훈 bfs
while queue_j:
    cx, cy = queue_j.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            print(jh[cx][cy] + 1)
            exit(0)
        if board[nx][ny] == "#" or jh[nx][ny] >= 0:
            continue
        if fire[nx][ny] <= jh[cx][cy] + 1 and fire[nx][ny] != -1:
            continue
        jh[nx][ny] = jh[cx][cy] + 1
        queue_j.append([nx, ny])
print("IMPOSSIBLE")