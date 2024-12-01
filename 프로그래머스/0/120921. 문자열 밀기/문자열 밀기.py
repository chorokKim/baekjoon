from collections import deque

def solution(A, B):
    answer = 0
    A = deque(A)
    B = deque(B)
    while A != B:
        if answer == len(A):
            return -1
        A.rotate(1)
        answer += 1
    return answer