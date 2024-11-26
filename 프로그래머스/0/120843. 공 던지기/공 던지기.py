from collections import deque
def solution(numbers, k):
    numbers = deque(numbers)
    for i in range(k-1):
        numbers.append(numbers.popleft())
        numbers.append(numbers.popleft())
    return numbers[0]