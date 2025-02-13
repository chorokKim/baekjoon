from sys import stdin


def start_index(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start
        

def end_index(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return start
        

N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
cards.sort()
M = int(stdin.readline())
arrM = list(map(int, stdin.readline().split()))
for m in arrM:
    print(end_index(cards, m) - start_index(cards, m), end=' ')