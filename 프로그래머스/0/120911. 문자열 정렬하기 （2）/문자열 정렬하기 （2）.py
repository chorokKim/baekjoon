def solution(my_string):
    my_string = my_string.lower()
    my_string = sorted([ord(string) for string in my_string])
    return ''.join([chr(i) for i in my_string])