# 문자열 변수를 초기화할 때 큰따옴표나 작은 따옴표를 이용
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 변수에 덧셈을 이용하면 문자열이 더해져서 연결
a = "Hello"
b = "World"
print(a + " " + b)

# 곱셈을 이용해서 문자열을 반복 가능
a = "String"
print(a*3)

# 문자열에 대해서도 마찬가지로 인덱싱과 슬라이싱을 이용 가능
# 다만 문자열은 특정 인덱스만 변경 할 수 없다.
a = "ABCDEF"
print(a[2:4])

# a[2] = 'a'
# print(a)

# 튜플 자료형 : 리스트와 유사
# 한번 선언된 값은 변경할 수 없음.
# 튜플은 소괄호를 이용
# 리스트에 비해 상대적으로 공간 효율적
# 튜플 사용 좋은 이유 : 서로 다른 성질의 데이터를 묶어서 관리할때

# 최단 경로 알고리즘에서 (비용, 노드번호)의 형태로 튜플 자료형 자주 사용
# 데이터의 나열을 해싱의 키 값으로 사용해야 할 때
# 리스트 보다 메모리를 효과적으로 사용해야 할 때

a = (1,2,3,4,5,6,7,8,9)

print(a[3])
print(a[1:4])
# a[2] = 7 불가능

'''
리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
'''