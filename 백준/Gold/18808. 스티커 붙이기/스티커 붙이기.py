from sys import stdin


N, M, K = map(int, stdin.readline().split())
laptop = [[0 for _ in range(M)] for _ in range(N)]
R, C = 0, 0
sticker = []

def is_available(x, y):
    for i in range(R):
        for j in range(C):
            if laptop[x + i][y + j] == 1 and sticker[i][j] == 1:
                return False
    return True

def paste(x, y):
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                laptop[x + i][y + j] = 1

def rotate():
    global sticker, R, C
    result = []
    for i in range(C):
        temp = []
        for j in range(R-1, -1, -1):
            temp.append(sticker[j][i])
        result.append(temp)
    R, C = C, R
    sticker = result


for _ in range(K):
    R, C = map(int, stdin.readline().split())
    for _ in range(R):
        row = list(map(int, stdin.readline().split()))
        sticker.append(row)

    for _ in range(4):
        is_paste = False
        for x in range(N - R + 1):
            if is_paste:
                break
            for y in range(M - C + 1):
                if is_available(x, y):
                    paste(x, y)
                    is_paste = True
                    break
        if is_paste:
            break
        rotate()
    sticker = []
cnt = 0
for i in range(N):
    for j in range(M):
        if laptop[i][j] == 1:
            cnt += 1
print(cnt)