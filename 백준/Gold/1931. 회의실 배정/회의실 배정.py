from sys import stdin

N = int(stdin.readline())
schedule = []
for _ in range(N):
    schedule.append(list(map(int, stdin.readline().split())))

schedule.sort(key=lambda schedule: (schedule[1], schedule[0]))

cnt = 0
end = 0
for s, e in schedule:
    if s >= end:
        cnt += 1
        end = e
print(cnt)