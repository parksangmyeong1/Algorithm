import sys
from itertools import combinations

n, m = map(int, input().split())

maps=[]
for i in range(n):
  maps.append(list(map(int, input().split())))

result = []
home=[]
chicken=[]

for i in range(n):
  for j in range(n):
    if maps[i][j] == 1:
      home.append((i, j))

    elif maps[i][j] == 2:
      chicken.append((i, j))

pick_chicken = list(combinations(chicken, m))

for chi in pick_chicken:
    temp = 0
    for h in home:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    result.append(temp)
    
print(min(result))