from sys import stdin

L = list(input())
R = []
M = int(input())

for _ in range(M):
    command = stdin.readline().split()
    try:
        if command[0] == "L":
            R.append(L.pop())
        elif command[0] == "D":
            L.append(R.pop())
        elif command[0] == "B":
            L.pop()
        else:
            L.append(command[-1])
    except IndexError:
        pass

print(''.join(L+R[::-1]))