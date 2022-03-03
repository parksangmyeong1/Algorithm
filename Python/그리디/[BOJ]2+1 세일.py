n = int(input())
list = []

for i in range(n):
    list.append(int(input()))

list.sort(reverse=True)
count = 1
result = 0

for i in range(n):
    if count % 3 == 0:
        count += 1
        continue
    else:
        result += list[i]
        count += 1
        
print(result)