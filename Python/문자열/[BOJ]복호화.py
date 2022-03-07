t = int(input())

for i in range(t):
    s = input().replace(' ', '')
    arr = [0] * 26
    
    for j in s:
        arr[ord(j) - 97] += 1
    
    if arr.count(max(arr)) > 1:
        print('?')
    else:
        print(chr(97 + arr.index(max(arr))))