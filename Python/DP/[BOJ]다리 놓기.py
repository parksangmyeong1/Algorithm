# 팩토리얼 문제 풀이

import sys
input = sys.stdin.readline

def Factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    bridge = Factorial(m) // (Factorial(m - n) * Factorial(n))
    print(bridge)

####################################################################################

# 팩토리얼 라이브러리 사용

import math
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    bridge = math.factorial(m) // (math.factorial(m - n) * math.factorial(n))
    print(bridge)

####################################################################################    

# DP 사용

import sys
input = sys.stdin.readline

t = int(input())

dp = [[0 for _ in range(31)] for _ in range(31)]
dp[0][0] = 1

for num in range(1,31):
    dp[num][0] = 1
    for pick in range(1,31):        
        dp[num][pick] = dp[num-1][pick] + dp[num-1][pick-1]

for i in range(t):
    n, m = list(map(int,input().split()))
    print(dp[m][n])