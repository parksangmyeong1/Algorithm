n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(dp[i][j])
            break

        num = arr[i][j]
        
        if i + num < n:
            dp[i + num][j] += dp[i][j]
            
        if j + num < n:
            dp[i][j + num] += dp[i][j]