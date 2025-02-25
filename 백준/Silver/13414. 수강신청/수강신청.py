from sys import stdin

K, L = map(int, stdin.readline().split())
students = {}
for i in range(L):
    s = stdin.readline().strip()
    students[s] = i

students = sorted(students.items(), key=lambda x: x[1])
for i in range(min(K, len(students))):
    print(students[i][0])