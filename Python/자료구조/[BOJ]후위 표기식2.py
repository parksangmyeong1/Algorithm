from collections import deque

n = int(input()) # 첫째줄 n 입력
s = input() # 입력한 문자열
stack = deque() # 덱을 이용한 
dic = {} # 알파벳과 입력한 정수를 매칭
num = []

for i in range(n): # stack에 매칭하려는 정수들 삽입
    stack.append(int(input()))

for i in s: # stack 정수들과 알파벳을 dic에 매칭
    if i not in dic and i.isalpha(): # 조건 : dic에 중복 금지, 알파벳만 적용
        dic[i] = stack.popleft()

for i in s:
    if i.isalpha(): # 입력한 문자열이 알파벳이면 매칭된(dic) 숫자를 num에 삽입
        num.append(dic[i])

    else: # 특수문자에 따라 연산 후 다시 삽입 반복
        a = num.pop()
        b = num.pop()
        if i == '+':
            num.append(b+a)
        elif i == '-':
            num.append(b-a)
        elif i == '*':
            num.append(b*a)
        elif i == '/':
            num.append(b/a)

print('%.2f' %float(num[0])) # 최종적으로 num에 남은 숫자가 결과값