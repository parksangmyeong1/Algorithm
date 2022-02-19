# 스택 : 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
# 입구와 출구가 동일한 형태로 스택을 시각화

stack = [] # 리스트 이용

# 5 - 2 - 3 - 7 - 삭제 - 1 - 4 - 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

# 큐 : 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
# 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화
# 라이브러리 사용없이 리스트로 큐 구현 가능하지만 시간 복잡도가 높아서 비효율적

from collections import deque

# 큐 구현을 위해 depue 라이브러리 사용
queue = deque()

# 5 - 2 - 3 - 7 - 삭제 - 1 - 4 - 삭제
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력