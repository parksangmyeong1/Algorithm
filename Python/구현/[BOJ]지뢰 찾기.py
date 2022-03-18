import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(input() for i in range(n))
arr2 = list(input() for i in range(n))
result = [['.'] * n for i in range(n)]

# 이동 범위
dx = [-1, -1, -1, 0, 1, 1, 1, 0] 
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def findboom(): # 지뢰 찾기 함수
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '.' and arr2[i][j] == 'x':
                boom = 0

                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue

                    if arr1[nx][ny] == '*':
                        boom += 1

                result[i][j] = boom

            if arr1[i][j] == '*' and arr2[i][j] == 'x': # 지뢰 밟은 경우
                makeFail()

def makeFail(): # 지뢰 밟은 경우 함수
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '*':
                result[i][j] = '*'

findboom()
for i in range(n):
    for j in range(n):
        print(result[i][j], end='')
    print()