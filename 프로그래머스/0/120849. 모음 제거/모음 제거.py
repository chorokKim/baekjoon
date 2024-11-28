def solution(my_string):
    answer = ''
    for string in my_string:
        if string not in ["a", "e", "i", "o", "u"]:
            answer += string
    return answer