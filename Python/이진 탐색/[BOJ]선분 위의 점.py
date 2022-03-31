import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline # 시간 제한을 위해 필요

n,m = list(map(int, input().split()))
array = list(map(int, input().split()))
array.sort()

for i in range(m):
    start, end = list(map(int, input().split()))
    left_index = bisect_left(array, start)
    right_index = bisect_right(array, end)
    print(right_index-left_index)