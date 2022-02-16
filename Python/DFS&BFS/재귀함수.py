# 재귀함수 : 자기 자신을 다시 호출하는 함수
# 어느 정도 출력하다가 최대 재귀 깊이 초과 오류 메시지(아래)가 출력된다.
# maximum recursion depth exceeded while calling a Python object
# 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 반드시 명시해야함.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
# -> 스택을 사용해야 할 때 구현상 스택 라이브러리 대신 재귀 함수를 이용하는 경우가 많음.

# 단순한 재귀 함수
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# 종료 조건을 포함한 재귀 함수 예제
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        print(i, '번째 재귀함수를 종료합니다.')
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

# 팩토리얼 구현 예제

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n=5)
print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))

# 최대공약수 계산(유클리드 호제법) 예제

def gcd(a,b):
    if a%b == 0:
        return
    else:
        return gcd(b, a%b)

print(gcd(192,162))