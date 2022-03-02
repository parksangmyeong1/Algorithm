input = input()
s = input.split('.')
check = True

for i in range(len(s)):
    if len(s[i]) % 4 == 0:
        s[i] = 'AAAA' * (len(s[i]) // 4)
    else:
        if len(s[i]) % 2 == 0:
            s[i] = 'AAAA' * (len(s[i]) // 4) + 'BB'
        else:
            check = False

if check:
    print('.'.join(s))
else:
    print(-1)