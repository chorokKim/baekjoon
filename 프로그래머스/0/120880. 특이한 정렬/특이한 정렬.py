def solution(numlist, n):
    numlist.sort(reverse=True)
    numlist.sort(key=lambda k: abs(k - n))
    return numlist