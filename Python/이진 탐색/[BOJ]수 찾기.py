import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    start, end = 0, n - 1
    check = False

    while start <= end:
        mid = (start + end) // 2

        if num == array[mid]:
            print(1)
            check = True
            break
        
        elif num > array[mid]:
            start = mid + 1
        elif num < array[mid]:
            end = mid - 1 

    if not check:
        print(0)