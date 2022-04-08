import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
lst = list(map(int, input().split()))

cnt = 0 # 홀수 개수
start, end = 0, 0
size, size_max = 0, 0 # 현재 부분 수열 길이, 가장 긴 짝수 부분 수열 길이
flag = 1 # end가 마지막 지점(n-1)일 경우 0으로 바뀜

for start in range(n):
    while cnt <= k and flag: # 홀수 개수가 <= k and flag == 1 일 때
        if lst[end] % 2:
            if cnt == k: # 홀수 개수가 k이면 종료
                break

            cnt += 1
        size += 1
        
        if end == n - 1:
            flag = 0
            break
        
        end += 1
        
    if size_max < size - cnt: # 최대 길이 구하기
        size_max = size - cnt
        
    if lst[start] % 2:
        cnt -= 1
        
    size -= 1

print(size_max)