from sys import stdin

N = int(stdin.readline())

arr = []
answer = []
for _ in range(N):
    arr.append(stdin.readline().strip())

def is_available(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                return False
    return True

def cut(x, y, n):
    if n == 1:
        answer.append(arr[x][y])
        return
    if not is_available(x, y, n):
        n //= 2
        answer.append("(")
        cut(x, y, n)
        cut(x, y + n, n)
        cut(x + n, y, n)
        cut(x + n, y + n, n)
        answer.append(")")
        return
    answer.append(arr[x][y])
    return

cut(0, 0, N)
print(''.join(answer))