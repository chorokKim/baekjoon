from sys import stdin
from collections import deque


N = int(stdin.readline())

def area(board, vis):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    r, g, b = 0, 0, 0
    colour = "R"
    for x in range(N):
        for y in range(N):
            if vis[x][y] == 1:
                continue
            if board[x][y] == "R":
                r += 1
                colour = "R"
            elif board[x][y] == "G":
                g += 1
                colour = "G"
            else:
                b += 1
                colour = "B"

            vis[x][y] = 1
            queue.append([x, y])
            while queue:
                cx, cy = queue.popleft()
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if vis[nx][ny] == 1 or board[nx][ny] != colour:
                        continue
                    vis[nx][ny] = 1
                    queue.append([nx, ny])
    return r + g + b

board = []
gb_board = []
vis = []
gb_vis = []
for _ in range(N):
    row = stdin.readline().strip()
    board.append(row)
    gb_board.append(row.replace("G", "R"))
    vis.append([0] * N)
    gb_vis.append([0] * N)

colour = str(area(board, vis))
gb_colour = str(area(gb_board, gb_vis))
print(colour + " " + gb_colour)