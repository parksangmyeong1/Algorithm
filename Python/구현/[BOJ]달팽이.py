import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
result = [[0 for _ in range(n)] for _ in range(n)]
num = n*n
t_x, t_y, x,y = 0,0,0,0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

result[x][y] = num
num -= 1
i = 0

while num > 0:
    nx = dx[i % 4] + x
    ny = dy[i % 4] + y

    if 0 <= nx < n and 0 <= ny < n and result[nx][ny] == 0:
        result[nx][ny] = num
        
        if num == m:
            t_x, t_y = nx, ny
        
        x,y = nx,ny
        num -= 1
    
    else:
        i += 1

for n in result:
    print(*n)

print(t_x+1, t_y+1)