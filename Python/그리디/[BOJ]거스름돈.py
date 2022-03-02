n = int(input())
result = 0

if n < 5:
    if n % 2 != 0:
        result = -1
    else:
        result += n//2
else:
    if n % 5 == 0:
        result += n//5
        n = n%5
    else:
        result += n//5
        n = n%5
        
        if n % 2 == 0:
            result += n//2
        else:
            result += (n+5)//2 -1

print(result)