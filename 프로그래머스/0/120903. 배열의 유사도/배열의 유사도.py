def solution(s1, s2):
    answer = 0
    if len(s1) > len(s2):
        for el in s2:
            if el in s1:
                answer += 1
    else:
        for el in s1:
            if el in s2:
                answer += 1      
    return answer