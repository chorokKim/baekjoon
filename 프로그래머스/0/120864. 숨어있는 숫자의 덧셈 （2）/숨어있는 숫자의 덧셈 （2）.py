import re
def solution(my_string):
    answer = map(int, re.findall("\d+", my_string))
    return sum(answer)