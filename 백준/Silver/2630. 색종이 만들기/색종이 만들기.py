from sys import stdin

N = int(stdin.readline())

paper = []
cnt = [0, 0]
for _ in range(N):
    paper.append(list(map(int, stdin.readline().split())))

def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def cut(x, y, n):
    if check(x, y, n):
        cnt[paper[x][y]] += 1
        return
    n = n // 2
    for i in range(2):
        for j in range(2):
            cut(n * i + x, n * j + y, n)


cut(0, 0, N)
for c in cnt:
    print(c)