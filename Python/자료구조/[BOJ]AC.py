import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    p = input()
    n = int(input().rstrip())
    arr = deque(input().rstrip()[1:-1].split(','))

    if n == 0:
        arr = deque()
    
    check = False

    for j in p:
        if j =='R':
            arr.reverse()
        elif j =='D':
            if arr:
                arr.popleft()
            else:
                print('error')
                check = True
                break
    if not check:
        print('[' + ','.join(arr) + ']')
