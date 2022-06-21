import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))
target = int(input().rstrip())
arr.sort()
start, end, count = 0 , n-1, 0

while start < end:
    num = arr[start] + arr[end]
    
    if num == target:
        count += 1
        start += 1

    elif num < target:
        start += 1

    else:
        end -= 1

print(count)