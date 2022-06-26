import sys
input = sys.stdin.readline

n = int(input().rstrip())

table = [list(map(int, input().split())) for i in range(n)]

dp = [0 for i in range(n+1)]

for i in range(n-1 , -1, -1):
    if i + table[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(table[i][1] + dp[i + table[i][0]], dp[i+1])
        
print(dp[0])