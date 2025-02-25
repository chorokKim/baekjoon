from sys import stdin

N, M = map(int, stdin.readline().split())
id_to_name = {}
name_to_id = {}
for i in range(1, N + 1):
    p = stdin.readline().strip()
    id_to_name[str(i)] = p
    name_to_id[p] = str(i)

for _ in range(M):
    inp = stdin.readline().strip()
    if inp.isdigit():
        print(id_to_name[inp])
    else:
        print(name_to_id[inp])