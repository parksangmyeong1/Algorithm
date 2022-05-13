import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    num = int(input())

    if num:
        hq.heappush(heap, (abs(num), num))

    else:
        if len(heap) > 0:
            print(hq.heappop(heap)[1])
        
        else:
            print(0)