import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr1 = list(map(int,input().rstrip().split()))
arr2 = list(map(int,input().rstrip().split()))

arr1.sort()
arr2.sort(reverse=True)
sum = 0
for i in range(n):
    sum += arr1[i] * arr2[i]
print(sum)