'''
내장함수 : 기본 입출력 부터 정렬까지 기본적인 함수들
itertools : 파이썬에서 반복되는 형태의 데이터를 처리, 순열과 조합 라이브러리
heapq : 힙 자료구조, 우선순위 큐 기능을 구현하기 위해
bisect : 이진 탐색 기능
coellections : 덱, 카운터 등의 유용한 자료구조
math : 필수적인 수학적 기능, 팩터리얼, 제곱근, 최대공약수, 삼각함수 등등
'''


array = [1,2,3,4,5]
array1 = [7,5,2,4]

# sum()
print(sum(array))

# min(),max()
print(min(array1),max(array1))

# eval() : 수학 수식(문자열 형태) 계산 결과 반환
print(eval("(3+5)*7"))

#sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 35), ('이순신',75),('아무개',50)]
result = sorted(array, key=lambda x:x[1], reverse=True)
print(result)

# 순열과 조합
# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열 nPr
# 조합 : 서로 다른 n개에세 순서에 상관 없이 서로 다른 r개를 선택 nCr

from itertools import permutations

data = ['A', 'B', 'c'] # 데이터 준비

result = list(permutations(data,3)) # 모든 순열 구하기
print(result)

from itertools import combinations

result = list(combinations(data,2)) # 2개를 뽑는 모든 조합 구하기
print(result)

from itertools import product

# 2개를 뽑는 모든 순열 구하기 (중복 허용)
result = list(product(data, repeat=2)) 
print(result)

from itertools import combinations_with_replacement

# 2개를 뽑는 모든 조합 구하기 (중복 허용)
result = list(combinations_with_replacement(data,2))
print(result)

# counter : 등장 횟수를 세는 기능
# 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 
# 내부의 원소가 몇 번씩 했는지 확인

from collections import Counter

# Counter객체 생성
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter)
print(counter['blue']) # blue가 등장한 횟수 출력
print(counter['red']) # red가 등장한 횟수 출력
print(counter['green']) # green이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환

counter = Counter('Hello World') # 대소문자 구분되어서 나옴
print(counter)

import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a,b):
    return a*b // math.gcd(a,b)

a,b=21,14

print(math.gcd(21,14)) # 최대 공약수(GCD) 계산
print(lcm(21,14)) # 최소 공배수(LCM) 계산
print(lcm(a,b))
print((lambda a,b: a*b // math.gcd(a,b))(a,b)) # 람다식으로 표현