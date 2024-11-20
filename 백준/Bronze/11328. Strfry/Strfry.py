N = int(input())

for _ in range(N):
    count = [0 for _ in range(26)]
    string1, string2 = input().split(" ")
    for s in string1:
        count[ord(s) - ord('a')] += 1
    for s in string2:
        count[ord(s) - ord('a')] -= 1
    if all(cnt == 0 for cnt in count):
        print("Possible")
    else:
        print("Impossible")