n = int(input())

list = list(map(int,input().split()))
list.sort(reverse=True)
arr = []
m = list[0]

if n == 1:
    arr.append(list[0])

for i in range(0,int(n/2)):
    if n % 2 == 0:
        arr.append(list[i]+list[n-i-1])
    else:
        arr.append(list[i+1]+list[n-i-1])

if m < max(arr):
    print(max(arr))
else:
    print(m)