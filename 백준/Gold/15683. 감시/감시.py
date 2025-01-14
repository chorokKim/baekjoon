from sys import stdin


N, M = map(int, stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
vis = []
cctv = []
answer = 0

def upd(x, y, dir):
    dir %= 4
    while True:
        x += dx[dir]
        y += dy[dir]
        if x < 0 or x >= N or y < 0 or y >= M or vis[x][y] == 6:
            return
        if vis[x][y] != 0:
            continue
        vis[x][y] = 7


for x in range(N):
    row = list(map(int, stdin.readline().split()))
    board.append(row)
    temp = []
    for y in range(M):
        if row[y] > 0 and row[y] < 6:
            cctv.append([x, y])
        elif row[y] == 0:
            answer += 1
        temp.append(-1)
    vis.append(temp)

for i in range(4**len(cctv)):
    for x in range(N):
        for y in range(M):
            vis[x][y] = board[x][y]
    brute = i
    for c in cctv:
        dir = brute % 4
        brute //= 4
        x, y = c
        if board[x][y] == 1:
            upd(x, y, dir)
        elif board[x][y] == 2:
            upd(x, y, dir)
            upd(x, y, dir + 2)
        elif board[x][y] == 3:
            upd(x, y, dir)
            upd(x, y, dir + 1)
        elif board[x][y] == 4:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
        elif board[x][y] == 5:
            upd(x, y, dir)
            upd(x, y, dir + 1)
            upd(x, y, dir + 2)
            upd(x, y, dir + 3)
    val = 0
    for i in range(N):
        for j in range(M):
            if vis[i][j] == 0:
                val += 1
    answer = min(answer, val)
print(answer)