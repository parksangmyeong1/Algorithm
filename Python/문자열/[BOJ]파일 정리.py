n = int(input())
file = dict() # 사전 자료형

for i in range(n):
    extend = input().split('.')[1] # 슬라이싱 후 .뒤에만 삽입
    
    if not extend in file: # 처음이면 1
        file[extend] = 1
    else:                  # 처음이 아니면 1개씩 증가
        file[extend] += 1

file = sorted(file.items()) # 키 값을 반환

for key, value in file:
    print(key, value)