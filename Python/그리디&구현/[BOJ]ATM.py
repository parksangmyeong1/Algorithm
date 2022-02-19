n = int(input())
p = list(map(int, input().split()))
total = 0
sum = 0

p.sort()

for i in p:
    total += i
    sum += total

print(sum)