import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    cmd = input().split()
    
    if len(cmd) == 2:
        X = cmd[1]
    cmd = cmd[0]

    if cmd == 'push':
        q.append(X)
    
    elif cmd == 'pop':
        if q:
            print(q.popleft())
        else:
            print('-1')
    
    elif cmd == 'size':
        print(len(q))

    elif cmd == 'empty':
        if q:
            print('0')
        else:
            print('1')

    elif cmd == 'front':
        if q:
            print(q[0])
        else:
            print('-1')

    elif cmd == 'back':
        if q:
            print(q[-1])
        else:
            print('-1')