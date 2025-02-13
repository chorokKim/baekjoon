from sys import stdin


def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
        

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
unique = list(set(arr))
unique.sort()
for a in arr:
    print(binarySearch(unique, a), end=' ')