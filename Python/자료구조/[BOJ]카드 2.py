import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque()

for i in range(n,0,-1):
    q.append(i)

while len(q) >= 2:
    q.pop()
    q.rotate(1)

print(q.popleft())