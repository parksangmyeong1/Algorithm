# 파이썬 스타일 가이드라인에서는 공백문자 4개를 사용하는 것을 표준으로 설정

a = -5

if a >= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a >= -10")
else:
    print("-10 > a")

score = 50

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif score >= 70:
    print("학점 : C")
elif score >= 60:
    print("학점 : D")
elif score >= 50:
    print("학점 : F")

'''
비교 연산자
X==Y : 서로 같을 때 True
X!=Y : 서로 다를 때 True
X>Y : X가 Y보다 클 때 True
X<Y : X가 Y보다 작을 때 True
X>=Y : X가 Y보다 크거나 같을 때 True
X<=Y : X가 Y보다 작거나 같을 때 True
'''
'''
논리 연산자
X and Y : X와 Y가 모두 True 일때 True
X or Y : X와 Y 중 하나 이상 True일때 True
not X : X가 False 일때 True
'''

if True or False:
    print("Yes")
if True and False:
    print("Yes")

'''
다수의 데이터를 담는 자료형을 위해 in, not in 연산자가 사용
X in list : list 안에 x가 들어가 있을 때 True
X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 True
'''

'''
pass 키워드 : 아무것도 처리하고 싶지 않을 때 사용
Ex) 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는
부분을 비워놓고 싶을 경우
'''

a = 50

if a >= 30:
    pass
else:
    print("a < 30")

# 조건문의 간소화
# 실행될 소스코드가 한 줄일 경우, 굳이 줄 바꿈을 하지 않고도 사용
score = 85

if score >= 80: result = "Success"
else: result = "Fail"
print(result)

# 조건부 표현식
score = 85
result = "Success" if score >= 80 else "Fail"

print(result)

# if x > 0 and X <20 == if 0 < x < 20