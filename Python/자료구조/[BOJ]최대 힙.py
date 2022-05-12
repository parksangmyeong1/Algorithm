# heapq -> 원래 최소 힙만 지원
# [응용] 최대 힙

import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    num = int(input())

    if num:
        hq.heappush(heap, (-num, num)) # 튜플을 만들어서 push
    
    else:
        if len(heap) > 0:
            print(hq.heappop(heap)[1]) # 튜플로 삽입했기에 index 1 출력
        
        else:
            print(0)