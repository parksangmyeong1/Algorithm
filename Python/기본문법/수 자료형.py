# 양의 정수
a = 10000
print(a)

# 음의 정수
a = -7
print(a)

a = a + 5
print(a)

# 양의 실수
a= 157.97
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)
# 정수부가 0일 때 0을 생략
a=-.7
print(a)

# 지수 표현 방식 -> 실수형
a = 1e9
print(a)
a = 75.25e1
print(a)
a = 3957e-3
print(a)
# 실수형 -> 정수형
a = int(1e9)
print(a)

a=0.3+0.6
print(a)
if a==0.9:
    print(True)
else:
    print(False)
if round(a,1)==0.9:
    print(True)
else:
    print(False)

a=7
b=3
# 나누기
print(a/b)
# 나머지
print(a%b)
#몫
print(a//b)
# 거듭 제곱
print(a**b)
# 제곱근
print(a**0.5)