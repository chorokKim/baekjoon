from sys import stdin
from collections import deque

t = int(stdin.readline())
for _ in range(t):
    w, h = map(int, stdin.readline().split())
    building = []
    fire = []
    sg = []
    for _ in range(h):
        row = stdin.readline().strip()
        building.append(row)
        fire.append([-1] * w)
        sg.append([-1] * w)

    queue_f = deque()
    queue_sg = deque()
    for x in range(h):
        for y in range(w):
            if building[x][y] == "*":
                fire[x][y] = 0
                queue_f.append([x, y])
            elif building[x][y] == "@":
                sg[x][y] = 0
                queue_sg.append([x, y])
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue_f:
        cx, cy = queue_f.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if fire[nx][ny] > -1 or building[nx][ny] == "#":
                continue
            fire[nx][ny] = fire[cx][cy] + 1
            queue_f.append([nx, ny])

    escape = False
    while queue_sg:
        cx, cy = queue_sg.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= h or ny <0 or ny >= w:
                escape = True
                break
            if building[nx][ny] != "." or sg[nx][ny] > -1:
                continue
            if fire[nx][ny] <= sg[cx][cy] + 1 and fire[nx][ny] != -1:
                continue
            sg[nx][ny] = sg[cx][cy] + 1
            queue_sg.append([nx, ny])
        if escape:
            break

    if escape:
        print(sg[cx][cy] + 1)
    else:
        print("IMPOSSIBLE")