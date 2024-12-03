from sys import stdin

N = int(stdin.readline())
queue = [i for i in range(1, N + 1)]
head = 0
while head < len(queue) - 1:
    if head % 2 == 0:
        pass
    else:
        queue.append(queue[head])
    head += 1
print(queue[head])