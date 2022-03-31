import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
powerList, nameList = [], []

for i in range(n):
    name, power = input().split()
    power = int(power)

    if powerList and powerList[-1] == power: # 가장 처음 칭호만 저장하기 위해
        continue
    powerList.append(power)
    nameList.append(name)

def binary_search(p): # 이진 탐색 함수
    start = 0
    end = len(powerList) - 1 

    while start <= end:
        mid = (start + end) // 2
        
        if p > powerList[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    print(nameList[end+1])

for i in range(m):
    p = int(input())
    binary_search(p) 


#################################################################

# 다른 사람 풀이

import sys
from bisect import bisect_left # bisect 라이브러리 사용
input = sys.stdin.readline

n, m = map(int, input().split())
name = []
power = []

for _ in range(n):
    a, b = input().split()
    name.append(a)
    power.append(int(b))

for _ in range(m):
    print(name[bisect_left(power, int(input()))])