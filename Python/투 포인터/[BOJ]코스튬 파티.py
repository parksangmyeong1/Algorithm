

n, s = map(int,input().split())
cows = []
for _ in range(n):
    cows.append(int(input()))
cows.sort()

count = 0
start, end = 0, n-1

while start < end:
    if cows[start] + cows[end] <= s:
        count = count + end - start
    else:
        end -= 1
        start -= 1
    start += 1

print(count)