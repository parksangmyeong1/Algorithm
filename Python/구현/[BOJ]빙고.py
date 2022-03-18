import sys
input = sys.stdin.readline

def is_bingo(arr): # 빙고 개수 확인 함수
    count = 0 # 빙고의 총 개수
    cnt1 = 0
    cnt2 = 0

    for low in arr: # 가로 빙고 확인
        if low.count(0) == 5:
            count += 1

    for i in range(5): # 세로 빙고 확인
        y = 0
        
        for j in range(5):
            if arr[j][i] == 0:
                y += 1
        
            if y == 5:
                count += 1

    for i in range(5): # 대각 빙고 확인
        if arr[i][i] == 0:
            cnt1 += 1

        if cnt1 == 5:
            count += 1
    
    for i in range(5):
        if arr[i][4-i] == 0:
            cnt2 += 1
        
        if cnt2 == 5:
            count += 1

    return count

bingo = [list(map(int, input().split())) for i in range(5)] # 빙고판
numbers = [] # 부르는 번호
for i in range(5):
    numbers.extend(list(map(int, input().split())))
order = 0 # 몇 번째 번호인지

for num in numbers:
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num: # 번호를 부르면 해당 위치 0으로 치환
                bingo[i][j] = 0

                order += 1
                result = is_bingo(bingo) # 빙고 개수 대입

                if result >= 3: # 3개 이상 빙고면 출력과 함께 종료
                    print(order)
                    exit()