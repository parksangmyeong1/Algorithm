import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

array = list(map(int, input().split()))
count = 0
start = 0
end = n-1
array.sort()

while start < end:
    sum = array[start] + array[end]

    if sum < m:
        start += 1
        
    elif sum > m:
        end -= 1

    else:
        count += 1 
        start +=1
        end -= 1

print(count)