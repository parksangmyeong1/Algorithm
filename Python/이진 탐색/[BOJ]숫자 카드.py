n = int(input())
card = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))
card.sort() # 정렬

def binary_search(array, target, start, end): # 이진탐색
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1 
    return None 

for i in range(m):
    if binary_search(card, check[i], 0, n-1): # 만약 있으면 1 없으면 0
        print(1, end=' ')
    else:
        print(0, end=' ')