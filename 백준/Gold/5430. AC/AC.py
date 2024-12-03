from sys import stdin
from collections import deque

T = int(stdin.readline())
for _ in range(T):
    p = stdin.readline().strip()
    n = int(stdin.readline())
    arr = []
    num = ''
    for a in stdin.readline().strip():
        if a.isdigit():
            num += a
        else:
            if num != '':
                arr.append(num)
                num = ''
    arr = deque(arr)
    error = False
    r = 0
    for cmd in p:
        if cmd == "R":
            r += 1
        else:
            if len(arr) == 0:
                error = True
                break
            if r % 2 == 1:
                arr.pop()
            else:
                arr.popleft()
    if error:
        print("error")
    else:
        if r % 2 == 1:
            arr.reverse()
        print('['+','.join(arr)+']')