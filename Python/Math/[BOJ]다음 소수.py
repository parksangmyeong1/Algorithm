import math
import sys

def is_prime_number(x): # 소수 찾는 함수
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x % i ==0:
            return False

    return True
    
input = sys.stdin.readline
t = int(input())

for i in range(t):
    num = int(input())

    while True:
        if is_prime_number(num):
            print(num)
            break

        else:
            num += 1