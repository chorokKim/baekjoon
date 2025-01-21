from sys import stdin

s = int(stdin.readline())
scores = [0]
d = [[0, 0, 0]]
for _ in range(s):
    scores.append(int(stdin.readline()))
    d.append([0, 0, 0])
if s == 1:
    print(scores[1])
    exit(0)
d[1][1] = scores[1]
d[2][1] = scores[2]
d[2][2] = scores[1] + scores[2]

for i in range(3, s + 1):
    d[i][1] = max(d[i - 2][1], d[i - 2][2]) + scores[i]
    d[i][2] = d[i - 1][1] + scores[i]

print(max(d[s][1], d[s][2]))