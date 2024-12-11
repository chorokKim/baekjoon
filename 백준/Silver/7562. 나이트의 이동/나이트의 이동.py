from sys import stdin
from collections import deque

t = int(stdin.readline())
for _ in range(t):
    I = int(stdin.readline())
    cx, cy = map(int, stdin.readline().split())
    dest_x, dest_y = map(int, stdin.readline().split())

    board = [[-1] * I for _ in range(I)]
    board[cx][cy] = 0
    queue = deque([[cx, cy]])
    
    dx = [-2, -2, -1, 1, 2, 2, 1, -1]
    dy = [-1, 1, 2, 2, 1, -1, -2, -2]
    arrive = False
    while board[dest_x][dest_y] == -1:
        cx, cy = queue.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if board[nx][ny] != -1:
                continue
            board[nx][ny] = board[cx][cy] + 1
            queue.append([nx, ny])
    print(board[dest_x][dest_y])