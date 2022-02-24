def is_prime_number(x): # 소수 찾는 함수
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

n = int(input())
s = map(int, input().split())
count = 0 # 소수의 개수

for i in s: # 입력값들 반복 수행
    check = is_prime_number(i) # 조건 : 소수면 True, 아니면 False 
    
    if check: # 소수라면 개수 증가
        count += 1

print(count)