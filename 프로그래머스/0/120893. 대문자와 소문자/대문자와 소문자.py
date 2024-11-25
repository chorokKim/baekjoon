def solution(my_string):
    answer = ''
    for string in my_string:
        answer += string.lower() if string.isupper() else string.upper()
    return answer