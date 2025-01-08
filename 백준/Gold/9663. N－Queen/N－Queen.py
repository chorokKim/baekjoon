from sys import stdin

N = int(stdin.readline())
isused1 = [False] * N
isused2 = [False] * N * 2
isused3 = [False] * N * 2
count = 0


def backtracking(cur):
    global count
    if cur == N:
        count += 1
        return
    for i in range(N):
        if isused1[i] or isused2[cur + i] or isused3[N - 1 + cur - i]:
            continue
        isused1[i] = True
        isused2[cur + i] = True
        isused3[N - 1 + cur - i] = True

        backtracking(cur + 1)

        isused1[i] = False
        isused2[cur + i] = False
        isused3[N - 1 + cur - i] = False

backtracking(0)
print(count)