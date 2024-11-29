def solution(before, after):
    cnt = [0 for _ in range(26)]
    for i in before:
        cnt[ord(i) - ord("a")] += 1
    for i in after:
        cnt[ord(i) - ord("a")] -= 1
    return 1 if all([c == 0 for c in cnt]) else 0