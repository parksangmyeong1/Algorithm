arr = []
result = ''
length = 0

for i in range(5):
    s = input()
    length = max(length, len(s))
    arr.append(s)

for i in range(length):
    for j in range(5):
        if len(arr[j]) <= i:
            continue
        result += arr[j][i]

print(result)