t = int(input())

dp= [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4,11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in range(t):
    n = int(input())

    print(dp[n])

##################################################################

# 재귀함수 이용 풀이

t = int(input())

def sol(n) : 
    if n == 1 :
        return 1
    
    elif n == 2 :
        return 2
    
    elif n == 3 :
        return 4
    
    else :
        return sol(n-1) + sol(n-2) + sol(n-3)

for i in range(t) : 
    n = int(input())
    print(sol(n))