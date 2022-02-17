n = input().split('-') # -로 구분
num = []

for i in n:
    sum = 0
    s = i.split('+') # (괄호)로 숫자들을 묶어준다.

    for j in s:
        sum += int(j)
    num.append(sum)

n = num[0]
for i in num[1:]:
    n -= i

print(n)