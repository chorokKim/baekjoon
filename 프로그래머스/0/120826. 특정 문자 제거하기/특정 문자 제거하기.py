def solution(my_string, letter):
    answer = ''.join([string for string in my_string if string != letter])
    return answer