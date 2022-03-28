s = int(input())
n = 1

while n * (n + 1) / 2 <= s: # 1부터 n까지의 합 공식 이용
    n += 1

print(n - 1)

##############################################################

# 다른 사람 풀이
s = int(input()) 
N = 0 
result = 0 

for i in range(1,s+1): 
    result += i 
    N += 1 

    if(result > s): 
        N -= 1 
        break

print(N)
