n = int(input())

check = False
s = []
result = []
count = 1

for i in range(n):
    num = int(input())

    while count <= num:
        s.append(count)
        result.append('+')
        count += 1

    if s[-1] == num:
        s.pop()
        result.append('-')
    else:
        check = True

if check:
    print('NO')
else:
    for i in result:
        print(i)