import sys
input = sys.stdin.readline

n = int(input())
dp = [10e9] * 300001
nums = [1]
i, j, k = 1, 1, 1

while k < n:
    i += 1
    j += i
    k += j

    nums.append(k)

for i in range(1, n+1):
    for num in nums:
        if num == i:
            dp[i] = 1
            break

        if num > i:
            break

        dp[i] = min(dp[i], dp[i-num] + 1)

print(dp[n])