n = int(input())
result = 0
honey_place = list(map(int,input().split()))
prefix_sum = []
prefix_sum.append(honey_place[0])

for i in range(1, n):
  prefix_sum.append(prefix_sum[i-1] + honey_place[i])

# 꿀통이 왼쪽 끝
for i in range(1, n-1):
  result = max(result,prefix_sum[n-2] + prefix_sum[i-1] - honey_place[i])

# 꿀통이 오른쪽 끝
for i in range(1, n-1):
  result = max(result, prefix_sum[n-1] - honey_place[0] + prefix_sum[n-1] - prefix_sum[i] - honey_place[i])

# 꿀통 가운데
for i in range(1, n-1):
  result = max(result,prefix_sum[n-2] - honey_place[0] + honey_place[i])

print(result)