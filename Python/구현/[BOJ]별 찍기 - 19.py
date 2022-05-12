n = int(input())

for i in range(1, n):
    num = 4 * (n - i) + 1
    print('* ' * (i - 1) + '*' * num + ' *' * (i - 1))
    print('* ' * i + ' ' * (num - 4) +  ' *' * i)

print('* ' * (n-1) + '*' + ' *' * (n-1))

for i in range(n-1, 0, -1):
    num = 4 * (n - i) + 1
    print('* ' * i + ' ' * (num - 4) +  ' *' * i)
    print('* ' * (i - 1) + '*' * num + ' *' * (i - 1))

######################################################################
# 다른 사람 풀이 - 재귀함수 사용

def draw(n, idx):
    if n == 1:
        starMap[idx][idx] = '*'
        return
    l = 4 * n -3
    
    
    for i in range(idx, l+idx):
    	#위 아래
        starMap[idx][i] = '*'
        starMap[idx+l-1][i] = '*'
        
        #양 옆
        starMap[i][idx] = '*'
        starMap[i][idx+l-1] = '*' 
 
    return draw(n-1, idx+2)
    
    
n = int(input())
lens = 4 * n -3

starMap = [[' '] * lens for _ in range(lens)]

draw(n,0)

for i in range(lens):
    for j in range(lens):
        print(starMap[i][j], end="")
    print()