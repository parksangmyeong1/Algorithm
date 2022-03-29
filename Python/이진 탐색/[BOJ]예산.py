n = int(input())

array = list(map(int,input().split()))
total = int(input())

start = 0
end = max(array)
ans = 0

if sum(array) <= total:
    print(end)
else:
    while start <= end:
        result = 0

        mid = (start + end) // 2

        for i in array:
            if i >= mid:
                result += mid
            else:
                result += i
        
        if result <= total:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    print(ans)