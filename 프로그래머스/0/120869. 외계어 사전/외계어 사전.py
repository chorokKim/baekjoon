def solution(spell, dic):
    answer = 0
    for word in dic:
        if set(spell) == set(word) and len(spell) == len(word):
            return 1
    return 2