from sys import stdin
from collections import deque

N = int(stdin.readline())
deque = deque()
for _ in range(N):
    cmd = stdin.readline().split()
    if cmd[0] == "push_front":
        deque.appendleft(cmd[1])

    elif cmd[0] == "push_back":
        deque.append(cmd[1])
        
    elif cmd[0] == "pop_front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())

    elif cmd[0] == "pop_back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())

    elif cmd[0] == "size":
        print(len(deque))

    elif cmd[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd[0] == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    else:
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])