# 반복문 while문
from array import array
import re


i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)

# 끊임없이 반복되는 반복 구문인 무한루프 조심
# 반복문을 작성한 뒤에는 항상 반복문을 탈출할 수 있는지 확인

'''
반복문 for문
for 변수 in 리스트:
    실행할 소스코드
'''

array = [9,8,7,6,5] # 리스트
for x in array:
    print(x)

array = (1,2,3,4,5) # 튜플
for x in array:
    print(x)

result = 0
for i in range(1,10):
    result += i
print(result)

# continue : 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행

# 1~9까지의 홀수의 합을 구할 때
result = 0
for i in range(1,10):
    if i % 2 ==0:
        continue
    result += i
print(result)

# 반복문을 즉시 탈출하고자 할 때 break 사용

#1부터 5까지의 정수를 차례대로 출력
i = 1

while True:
    print("현재 i의 값 : ", i)
    if i ==5:
        break
    i += 1
print("while문 탈출")

# 학생들의 합격 여부 판단 
scores = [90,85,77,65,97]
cheating_student_list = {2,4}

for i in range(5):
    if i+1 in cheating_student_list: # 특정 번호 학생 제외
        continue
    if scores[i]>80:
        print(i+1,"번 학생은 합격입니다.")

# 중첩된 반복문 : 구구단
for i in range(2,10):
    print(i,"단")
    for j in range(1,10):
        print(i, "X", j, "=", i*j)
