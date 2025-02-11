from sys import stdin

N = int(stdin.readline())
arrA = list(map(int, stdin.readline().split()))
arrA.sort()
M = int(stdin.readline())
arrM = list(map(int, stdin.readline().split()))

for m in arrM:
    start = 0
    end = N - 1
    result = False
    while start <= end:
        mid = (start + end) // 2
        if m < arrA[mid]:
            end = mid - 1
        elif m > arrA[mid]:
            start = mid + 1
        else:
            result = True
            break

    if result:
        print("1")
    else:
        print("0")