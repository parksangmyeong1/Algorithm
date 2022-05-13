import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    array = list(map(int, input().split()))

    if not heap: # 조건 없이 모든 수를 힙에 넣으면 메모리 부족
        for num in array:
            hq.heappush(heap, num)
    
    else:
        for num in array:
            if heap[0] < num:
                hq.heapreplace(heap, num)

print(heap[0])