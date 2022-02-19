n, k = map(int, input().split())

list = []
for i in range(1,n+1):
    list.append(i)

answer = []
index = k-1

for i in range(n):
    if len(list) > index:
        answer.append(list.pop(index))
        index += k-1
    else:
        index = index % len(list)
        answer.append(list.pop(index))
        index += k-1
        
print("<", ', '.join(str(i) for i in answer), ">", sep = '')

######################################################################

# <다른 풀이>
# 큐를 이용, 큐의 함수의 rotate함수 이용
# deque.rotate : 파이썬에서 목록을 회전시키는 가장 효율적인 방법
# 양수면 밀고, 음수면 당기기

from collections import deque

N, K = map(int, input().split())
list = []
q = deque([i + 1 for i in range(N)])

while len(q) != 0:
    q.rotate(-K)
    list.append(q.pop())

print('<' + ', '.join(map(str, list)) + '>')