# 1. 재귀함수 풀이

def fibonacci(num):
    if num <= 1:
        return num
        
    return fibonacci(num-1) + fibonacci(num-2)

n = int(input())
print(fibonacci(n))

###################################################################
# 2. for문 풀이
n = int(input())

fibonacci = [0, 1]

for i in range(2, n+1):
    num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(num)

print(fibonacci[n])