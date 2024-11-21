from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
result = []

idx = 0
while queue:
    idx += 1
    e = queue.popleft()
    if idx % K == 0:
        result.append(e)
    else:
        queue.append(e)

print("<", end="")
for i in range(len(result) - 1):
    print(result[i], end=", ")
print(str(result[-1])+">")