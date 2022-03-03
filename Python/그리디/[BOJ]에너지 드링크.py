n = int(input())

list = list(map(int,input().split()))
list.sort(reverse=True)

for i in range(1,n):
    list[0] += list[i]/2

print(list[0])