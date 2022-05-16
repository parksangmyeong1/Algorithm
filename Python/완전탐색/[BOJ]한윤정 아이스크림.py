import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
ice = [[False for _ in range(n)] for _ in range(n)]
result = 0

for i in range(m):
    ice1, ice2 = list(map(int, input().split()))
    ice[ice1 - 1][ice2 - 1] = True
    ice[ice2 - 1][ice1 - 1] = True

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1
print(result)