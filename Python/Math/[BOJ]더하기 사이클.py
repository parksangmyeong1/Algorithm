n = int(input())

result = n
count = 0

while True:
    n = (n % 10) * 10 + ((n // 10) + (n % 10)) % 10
    count += 1

    if result == n:
        break
    
print(count)