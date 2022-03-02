n, k = map(int,input().split())
count = 0
coins = []

for i in range(n):
    coins.append(int(input()))

for i in range(n-1,-1,-1):
    if coins[i] > k:
        continue
    count += k // coins[i]
    k = k % coins[i]

print(count)