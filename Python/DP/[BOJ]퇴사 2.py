import sys 
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)
t, p = [], []
for i in range(n):
    x, y = list(map(int, input().split()))
    t.append(x)
    p.append(y)
    
m = 0
for i in range(n):
    m = max(m, dp[i])

    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(m + p[i], dp[i + t[i]])

print(max(dp))