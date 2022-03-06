t = int(input())

for i in range(t):
    s = input().replace(' ', '')
    arr = [0] * 26
    for c in s:
        if c.isalpha:
            arr[ord(c)-ord('a')] += 1
    t = max(li)
    print()