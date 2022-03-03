n = int(input())
s = input()
result = 1

for i in range(n-1):
    if s[0] == 'B':
        if s[i:i+2]=='BR':
            result += 1
    else:
        if s[i:i+2]=='RB':
            result += 1

print(result)