import sys
input = sys.stdin.readline

arr = [0] * 10

word = input().rstrip()

for i in range(len(word)):
    num = int(word[i])
    
    if num in (6, 9):
        if arr[6] <= arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[num] += 1
print(max(arr))