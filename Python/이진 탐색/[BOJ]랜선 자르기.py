k, n = list(map(int, input().split()))

array = []

for i in range(k):
    array.append(int(input()))

start = 1 # m = 0이면 안되기에 1로 설정
end = max(array)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i >= mid:
            total += i // mid
        
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)