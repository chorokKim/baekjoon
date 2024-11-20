string1 = input()
string2 = input()

count = [0 for _ in range(26)]

for s in string1:
    count[ord(s) - ord('a')] += 1
for s in string2:
    count[ord(s) - ord('a')] -= 1

result = 0
for cnt in count:
    result += abs(cnt)
print(result)