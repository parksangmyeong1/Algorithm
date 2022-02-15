# 사전 자료형 : 키와 값의 쌍으로 데이터를 가지는 자료형
# 파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에
# 있어서 O(1)상수의 시간에 처리할 수 있음.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

data2 = {'name':'park', 'tel':'01012345678', 'birth':'950324'}

print(data)
print(data2)
if '사과' in data:
    print("'사과'를 키로 가지고 있는 데이터가 존재합니다.")

# 키 데이터만 뽑아서 리스트로 이용할 때는 keys()함수를 이용
# 값 데이터만 뽑아서 리스트로 이용할 때는 values()함수를 이용

# 키 데이터만 담은 리스트
key_list = list(data.keys())
# 값 데이터만 담은 리스트
value_list = list(data.values())
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 집합 : 중복을 허용하지 않고, 순서가 없다. 
# -> 어떤 데이터가 존재하는지 여부만을 확인할때 효과적
# 리스트 혹은 문자열을 초기화 : set()
# 혹은 중괄호{} 안에 각 원소를 , 를 기준으로 구분하여 삽임함으로써 초기화
# 데이터의 조회 및 수정에 있어서 O(1)의 상수의 시간에 처리

# 집합 자료형 초기화 1
data = set([1,1,2,3,4,4,5])
print(data)
# 집합 자료형 초기화 2
data = {1,1,2,3,4,4,5}
print(data)

# 합집합, 교집합, 차집합

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b)
print(a&b)
print(a-b)

data = set([1,2,3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 제거
data.remove(3)
print(data)

'''
사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱을 통해 값을 얻을 수 없음
사전의 키 혹은 집합의 원소를 통해 O(1)상수의 시간 복잡도로 조회 가능
'''