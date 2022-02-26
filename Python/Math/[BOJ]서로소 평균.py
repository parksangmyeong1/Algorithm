def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

n = int(input())
a = list(map(int, input().split()))
x = int(input())
result = []

for i in a:
    if gcd(x,i) == 1:
        result.append(i)

print(sum(result)/len(result))