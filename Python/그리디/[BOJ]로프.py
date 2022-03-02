n = int(input())
list = []
result = []

for i in range(n):
    list.append(int(input()))

list.sort(reverse=True)

for i in range(n):
    result.append(list[i]*(i+1))

print(max(result))