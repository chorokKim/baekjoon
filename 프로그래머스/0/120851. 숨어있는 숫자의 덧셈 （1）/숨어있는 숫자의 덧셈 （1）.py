import re

def solution(my_string):
    answer = sum(map(int, re.findall("\d", my_string)))
    return answer