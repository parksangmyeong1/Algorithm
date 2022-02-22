from collections import deque

n = int(input())
q = deque()
result = []
arr = list(map(int, input().split()))
for i in range(n):
    q.append(i+1)

while q:
    check = q.popleft()
    result.append(check)

    if arr[check-1] > 0:
        for i in range(arr[check-1]-1):
            q.rotate(-1)

    else:
        for i in range(abs(arr[check-1])):
            q.rotate(1)

print(' '.join(map(str, result)))