case = int(input())

for _ in range(case):
    L = []
    R = []
    command = list(input())
    for cmd in command:
        try:
            if cmd == "<":
                R.append(L.pop())
            elif cmd == ">":
                L.append(R.pop())
            elif cmd == "-":
                L.pop()
            else:
                L.append(cmd)
        except IndexError:
            pass

    print(''.join(L+R[::-1]))