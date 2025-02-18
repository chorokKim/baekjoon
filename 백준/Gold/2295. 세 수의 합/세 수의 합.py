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
            return True
    return False
        

N = int(stdin.readline())
U = [int(stdin.readline()) for _ in range(N)]
U.sort()

two = []
for i in range(N):
    for j in range(N):
        two.append(U[i] + U[j])
two.sort()

for i in range(N - 1, -1, -1):
    for j in range(N):
        if binarySearch(two, U[i] - U[j]):
            print(U[i])
            exit(0)