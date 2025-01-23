from sys import stdin
from collections import deque


def is_available(sel):
    group = [[0] * 5 for _ in range(5)]
    vis = [[0] * 5 for _ in range(5)]
    for s in sel:
        group[s[0]][s[1]] = 1

    queue = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue.append(sel[0])
    vis[sel[0][0]][sel[0][1]] = 1
    cnt = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if group[nx][ny] == 0 or vis[nx][ny] == 1:
                continue
            queue.append([nx, ny])
            vis[nx][ny] = 1
            cnt += 1
    return True if cnt == 7 else False

def backtracking(depth, k, yeon):
    global answer
    if yeon >= 4:
        return
    if depth == 7:
        if is_available(sel):
            answer += 1
        return
    for i in range(k, 25):
        x = i // 5
        y = i % 5
        sel.append([x, y])
        backtracking(depth + 1, i + 1, yeon + (board[i] == "Y"))
        sel.pop()

board = ''
for _ in range(5):
    board += stdin.readline().strip()
answer = 0
sel = []
backtracking(0, 0, 0)
print(answer)