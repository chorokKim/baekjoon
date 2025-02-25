from sys import stdin

n = int(stdin.readline())
company = {}
while n > 0:
    name, state = stdin.readline().split()
    if state == "enter":
        company[name] = "enter"
    else:
        del company[name]
    n -= 1
company = list(company.keys())
company.sort(reverse=True)
for c in company:
    print(c)