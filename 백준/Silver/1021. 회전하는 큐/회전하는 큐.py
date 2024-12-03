from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
deque = deque([i for i in range(1, N + 1)])
sequence = list(map(int, stdin.readline().split()))

answer = 0
s = 0
while M > 0:
    idx = deque.index(sequence[s])
    if idx > len(deque) / 2:
        while deque[0] != sequence[s]:
            deque.rotate(1)
            answer += 1
    else:
        while deque[0] != sequence[s]:
            deque.rotate(-1)
            answer += 1
    deque.popleft()
    M -= 1
    s += 1
print(answer)