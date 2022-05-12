# list 풀이 : 시간복잡도 O(N)

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

array = []

for i in range(n):
    array.append(input().rstrip())

count = 0

for i in range(m):
    word = input().rstrip()
    
    if word in array:
        count += 1

print(count)

#############################################################################
# dict or set 풀이 : 시간복잡도 O(1) -> 해쉬를 이용해 접근속도 빠르다

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
count = 0
S = dict()

for i in range(n):
    index = input().rstrip()
    S[i] = index

for j in range(m):
    check = input().rstrip()
    
    if check in S:
        count += 1

print(count)

# set 풀이

import sys
input = sys.stdin.readline
 
n, m = list(map(int, input().split()))
count = 0
S = {input().rstrip() for _ in range(n)}
 
for j in range(m):
    if input().strip() in S:
        count += 1

print(count)