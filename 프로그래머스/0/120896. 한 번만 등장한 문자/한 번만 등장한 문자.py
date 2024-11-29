def solution(s):
    answer = ''
    for i in sorted(set(s)):
        if s.count(i) == 1:
            answer += i
    return answer