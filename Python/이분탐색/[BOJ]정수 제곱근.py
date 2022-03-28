n = int(input())

s = 0
e = n

while s <= e:
    mid = (s + e) // 2 # 중앙값

    if mid ** 2 < n: # 중간미만 이면 시작점 = 중간점 +1
        s = mid + 1
    
    else: # 중간 이상이면 끝점 = 중간점 -1
        e = mid - 1

print(s)