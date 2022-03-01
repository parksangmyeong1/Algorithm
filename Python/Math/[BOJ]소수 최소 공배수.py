import math
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
prime_number = []

def is_prime_number(x): # 소수 찾는 함수 // 시간 초과를 위해서 사용
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True

for i in range(len(a)):
    if is_prime_number(a[i]):
        prime_number.append(a[i])
    else:
        continue

if prime_number:
    lcm = prime_number[0]

    for j in range(1, len(prime_number)):
        lcm = math.lcm(prime_number[j], lcm)
    print(lcm)
else:
    print(-1)