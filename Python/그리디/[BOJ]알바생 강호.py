n = int(input())
list = []
result = 0

for i in range(n):
    list.append(int(input()))
list.sort(reverse=True)

for i in range(n):
    sum = list[i]-i

    if sum <0:
        continue
    else:
        result += sum

print(result)