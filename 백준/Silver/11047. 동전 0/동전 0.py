from sys import stdin

N, K = map(int, stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(stdin.readline()))

cnt = 0
for i in range(N - 1, -1, -1):
    coin = arr[i]
    while K >= coin:
        cnt += K//coin
        K %= coin
        
print(cnt)