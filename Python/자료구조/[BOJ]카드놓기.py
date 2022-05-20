from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
cards = [i for i in range(1, n+1)]

array = list(map(int, input().split()))

array.reverse()

for i in range(len(array)):
    if array[i] == 1:
        q.appendleft(cards[i])
    elif array[i] == 2:
        q.insert(1,cards[i])
    else:
        q.append(cards[i])

print(' '.join(map(str, q)))