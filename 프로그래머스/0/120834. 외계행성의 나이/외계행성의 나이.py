def solution(age):
    answer = ''
    for s in str(age):
        answer += chr(ord('a') + int(s))
    return answer