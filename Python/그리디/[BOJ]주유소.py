n = int(input())
distance,costs = list(map(int, input().split()))
costs = list(map(int, input().split()))
min = costs[0]
result = 0

for i in range(1,n):
    if min > costs[i]:
        result += min * distance[i-1]
        min = costs[i]
    else:
        result += min * distance[i-1]

print(result)