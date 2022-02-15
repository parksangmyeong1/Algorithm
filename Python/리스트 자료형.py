# 리스트 자료형
from array import array
from os import remove


a = [1,2,3,4,5,6,7,8,9]
print(a)

# 네 번째 원소만 출력
print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n=10
a = [0]*n
print(a)

b = [0]*10
print(b)

'''
인덱스 값을 입력하여 리스트의 특정한 원소에 접근하는 것 : 인덱싱 
파이썬의 인데스 값은 양의 정수 음의 정수 모두 가능
음의 정수를 넣으면 원소를 거꾸로 탐색
'''
# 리스트 원소를 바꿈
c=[2,3,5,2,6,7,8,2,6,4,2]
c[3] = 4
print(c)
# print(b[3]) 음의 정수로 접근
print(c[-7])

''' 
리스트에서 연속적인 위치를 갖는 원소들을 가져와야 할 때 : 슬라이싱
대괄호 안에 : 을 넣어서 시작 인덱스와 끝 인덱스 설정
끝 인덱스는 실제 인덱스 보다 +1 설정
'''

print(c[0:4])
print(c[:6])
print(c[2:])

'''
리스트 컴프리헨션 : 리스트를 초기화 하는 방법 중 하나
대괄호 안에 조건문과 반복문을 적용하여 리스트 초기화 가능
'''

array = [i+1 for i in range(10)]
print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 일반적인 코드
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1, 10)]
print(array)

'''
리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적
특히 N x M 크기의 2차원 리스트를 한번에 초기화 할 때 유용
'''

n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)
array[1][1] = 5
print(array)
# 출력값 [[0, 0, 0], [0, 5, 0], [0, 0, 0], [0, 0, 0]]

# 잘못된 리스트 초기화 방법
array = [[0]*m] * n

array[1][1] = 5
print(array)
# 출력값 [[0, 5, 0], [0, 5, 0], [0, 5, 0], [0, 5, 0]]

# 파이썬에서 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할때 _ 를 사용
for _ in range(5):
    print("Hello World!")

''' 리스트 관련 기타 메소드
append() : 리스트에 원소 삽입
sort() : 리스트 오름차순으로 정렬 / sort(reverse = True) -> 내림차순
reverse() : 리스트 원소의 순서를 모두 뒤집기
insert(인덱스, 값) : 특정한 인덱스 위치에 원소 삽입 
count(특정 값) : 특정한 값을 가지는 데이터의 개수 확인
remove(특정 값) 특정한 값을 갖는 원소를 제거, 원소가 여러 개면 하나만 제거
'''

a = [4,3,2,1]

a.reverse()
print(a)

a.insert(2,3)
print(a)

print(a.count(3))

a.remove(1)
print(a)

# 리스트에서 특정 값을 가지는 원소 모두 제거
a = [1,2,3,4,5,5,5]
remove_set = {3,5} # 집합 자료형

result = [i for i in a if i not in remove_set]
print(result)