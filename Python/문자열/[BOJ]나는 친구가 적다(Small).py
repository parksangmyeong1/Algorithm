s = input()
k = input()
arr = []

for ch in s:
    if ch.isalpha():
        arr.append(ch)

arr = ''.join(arr)

if k in arr:
    print(1)
else:
    print(0)