n = int(input())
s = []

for i in range(n):
    s.append(list(map(int, input().split())))

s = sorted(s, key = lambda a:(a[1],a[0]))
# s = sorted(s, key= lambda a:a[0])
# s = sorted(s, key= lambda a:a[1])

count = 0
last = 0

for i in s:
    if i[0] >= last:
        last = i[1]
        count += 1

print(count)