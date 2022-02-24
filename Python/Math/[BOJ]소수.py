m = int(input())
n = int(input())

def is_prime_number(x): # 소수 체크 함수
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

sum = 0 # 소수의 총합
arr = [] # 소수 리스트

for i in range(m,n+1):
    if i > 1: # 조건 : 소수가 아닌 1을 위해 설정
        check = is_prime_number(i)

        if check: # 조건 : 소수이면
            sum += i # 더하고
            arr.append(i) # 리스트에 추가

if arr: # 소수가 있다면 
    print(sum)
    print(min(arr))

else: # 소수가 없다면 -1 출력
    print(-1)