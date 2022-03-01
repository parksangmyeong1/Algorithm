import math

def is_prime_number(x): # 소수 찾는 함수
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

n = int(input())
result = 0

for i in range(n, 1000001):
  if i == 1:
    continue

  if str(i) == str(i)[::-1]:
    if is_prime_number(i):
      result = i
      break

if result == 0:
  result = 1003001

print(result)

#########################################################################

import sys
input = sys.stdin.readline

def is_palindrome(n): # 팰린드롬 확인 함수
    length = len(n) // 2
    for i in range(length):
        if n[i] != n[-i-1]:
            return False
    return True

def is_prime_number(n): # 소수 확인 함수
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

N = int(input())

while True:
    if is_palindrome(str(N)) and is_prime_number(N):
        break
    N += 1
print(N)