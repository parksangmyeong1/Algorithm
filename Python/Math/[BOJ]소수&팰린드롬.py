import math

def is_prime_number(x): # 소수 찾는 함수
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True

n = int(input())
result = 0

for i in range(n, 1000001) :
  if i == 1 :
    continue
  if str(i) == str(i)[::-1] :
    if is_prime_number(i) :
      result = i
      break

if result == 0 :
  result = 1003001

print(result)