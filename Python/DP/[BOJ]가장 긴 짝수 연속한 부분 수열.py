import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
lst = list(map(int, input().split()))

cnt = 0 # 홀수 개수
start, end = 0, 0
size, size_max = 0, 0 # 현재 부분 수열 길이, 가장 긴 짝수 부분 수열 길이
flag = 1 # end가 마지막 지점(n-1)일 경우 0으로 바뀜

for start in range(n):
    while cnt <= k and flag: # 홀수 개수가 <= k and flag == 1 일 때
        if lst[end] % 2:
            if cnt == k: # 홀수 개수가 k이면 종료
                break

            cnt += 1
        size += 1
        
        if end == n - 1:
            flag = 0
            break
        
        end += 1
        
    if size_max < size - cnt: # 최대 길이 구하기
        size_max = size - cnt
        
    if lst[start] % 2:
        cnt -= 1
        
    size -= 1

print(size_max)

######################################################################

# 다른 사람 풀이 -> DP

n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    s[i] %= 2
    
    for j in range(k+1):
        if s[i] == 0: #짝수일 때
            dp[i][j] = dp[i-1][j] + 1

        if j != 0 and s[i]: #홀수일 때 
            dp[i][j] = dp[i-1][j-1]
            
result = []

for i in dp:
    result.append(i[k])

print(max(result))