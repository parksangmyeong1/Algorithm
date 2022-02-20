s = input() # 쇠막대기와 레이저의 배치 입력

stack = []
result = 0 # 잘린 쇠막대기 수

for i in range(len(s)): # 입력된 배치만큼 반복하면서
    if s[i] == '(': # ( 라면 쇠막대기의 시작 의미 : 스택에 ( 삽입
        stack.append(s[i])

    else:
        if s[i-1] == '(': # ()레이저 라면 그전에 입력된 ( 제거하고 쌓인 스택(쇠막대기)만큼 결과값에 추가
            stack.pop()
            result += len(stack)
        else: # ))라면 쇠막대기의 끝을 의미 : 스택 하나 줄이고, 결과값에 +1
            stack.pop()
            result += 1

print(result) # 결과값 출력