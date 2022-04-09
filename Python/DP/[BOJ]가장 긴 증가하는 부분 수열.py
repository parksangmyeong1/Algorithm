n = int(input())
s = [0] + list(map(int, input().split()))
dp = [0] + [1 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if s[i] < s[j] and dp[i]>= dp[j]:
            dp[j] = dp[i] + 1

print(max(dp))