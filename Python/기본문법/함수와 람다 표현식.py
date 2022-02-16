# 함수 : 특정한 작업을 하나의 단위로 묶어 놓은 것
# 불필요한 소스코드의 반복을 줄임
'''
def 함수명(매개변수):
    실행할 소스코드
    return 반환 값
'''

from re import A


def add(a,b):
    return a+b
print(add(3,7))

def subtract(a,b):
    return a-b

def add(a,b):
    print('함수의 결과 : ', a+b)

add(3,7)
result = subtract(3,7)
print(result)
add(b=3,a=2)

# global : 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고,
# 함수 바깥에 선언된 변수를 바로 참조
# 같은 이름의 전역 변수 지역 변수가 존재하면 함수에서는 지역변수
# 함수 밖에서는 전역 변수를 사용

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 파이썬에서는 함수는 여러 개의 반환 값을 가질 수 있음.

def operator(a,b):
    add_var = a+b
    subtract_var = a-b
    multiply_var = a*b
    divide_var = a/b
    return add_var,subtract_var,multiply_var,divide_var

a,b,c,d = operator(7,3)
print(a,b,c,d)

# 람다표현식 : 특정한 기능을 수행하는 함수를 한 줄에 작성
# 효과적 : 함수 자체를 입력으로 받는 또다른 함수
# 간단한 또는 한번 사용되는 함수

print((lambda a,b: a+b)(3,7))
# 리스트가 튜플 형태
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

# 람다 표현식 예시 : 여러 개의 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = list(map(lambda a,b: a+b,list1,list2))

print(list(result))