t = int(input())

for i in range(t):
    arr = input()
    sum = 0

    for j in arr:
        if j == '(':
            sum += 1
        
        elif j == ')':
            sum -= 1

        if sum < 0:
            print('NO')
            break

    if sum == 0:
        print('YES')
    
    elif sum > 0:
        print('NO')