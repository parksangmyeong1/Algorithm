n,m = map(int, input().split())
listen, look = [],[]

for i in range(n):
    listen.append(input())

for i in range(m):
    look.append(input())

result = sorted(list(set(listen) & set(look)))

print(len(result))

for i in result:
    print(i)