# input() 함수는 한 줄의 문자열을 입력 받는 함수
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# map(function, iterable) map(적용시킬 함수, 적용할 값들(리스트,튜플))

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))
# 특정 개수에 입력받을 때
a,b,c = map(int, input().split( ))

print("a,b,c 출력 : " ,a,b,c)
print("n : ",n)
print("data : ", data)
data.sort(reverse=True)
print("data 내림차순 : ", data)

# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우 -> 시간 초과 판정을 위해
# 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메소드 이용
# 단, 입력후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메소드를 함께 사용

import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print("문자열 입력 결과 : ", data)

# 줄 바꿈을 원치 않는 경우 end 속성을 이용함.

print(7, end=" ")
print(8, end=" ")
# 출력할 변수
answer = 7
# 문자열과 정수형이 직접인 더하기 연산 불가하기 때문에 문자열로 바꾸고 출력
print("정답은 " + str(answer) + "입니다.")

# f-string : 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣음
# 파이썬 3.6부터 사용 가능, 문자열 앞에 접두사 f붙임
answer = 7
print(f"정답은 {answer}입니다.")
