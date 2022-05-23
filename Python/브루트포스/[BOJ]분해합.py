import sys
input = sys.stdin.readline

n = int(input().rstrip())
result = 0

for i in range(1, n+1):        
    li = list(map(int, str(i)))  
    s = i + sum(li)   

    if(s == n):                 
        result = i                   
        break

print(result)