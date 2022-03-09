n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr = list(set(arr)) # 중복 단어 제거
arr.sort(key= lambda x : (len(x), x)) # 1. 길이 2. 알파벳 순서

for i in arr:
    print(i)