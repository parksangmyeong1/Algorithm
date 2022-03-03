a,b = map(int,input().split())
count = 1

while True:
    if a > b:
        print(-1)
        break

    if b % 10 == 1:
        b = b // 10
        count += 1

    elif b % 2 == 0:
        b = b // 2
        count += 1

    else:
        print(-1)
        break
    
    if a == b:
        print(count)
        break