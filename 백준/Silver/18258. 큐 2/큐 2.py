from sys import stdin
from collections import deque

N = int(stdin.readline())
queue = deque()
for _ in range(N):
    cmd = stdin.readline().split()
    if cmd[0] == "push":
        queue.append(cmd[1])
        
    elif cmd[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif cmd[0] == "size":
        print(len(queue))

    elif cmd[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])