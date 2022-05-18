import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ice = [0] * 1000001

for i in range(n):
    g,x = map(int, input().split())
    ice[x] = g

step = 2 * k + 1
max_sum = sum(ice[:step])
result = max_sum

for i in range(step, 1000001):
    max_sum += (ice[i] - ice[i - step])
    result = max(result, max_sum)

print(result)