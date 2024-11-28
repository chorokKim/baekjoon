def solution(n):
    result = 1
    for i in range(1, 11):
        result *= i
        if result > n:
            return i - 1
        elif result == n:
            return i