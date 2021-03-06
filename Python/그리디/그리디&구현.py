# 그리디

# 문제> 1이 될 때까지
# 첫째 줄에 N(1 <= N <= 100000)과 K(2 <= K <= 100000)가 공백을
# 기준으로 하여 각각 자연수로 주어집니다.
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의
# 최솟값을 출력합니다.
# 1번 : N에서 1을 뺍니다.
# 2번 : N을 K로 나눕니다.
# 입력예시 : 25 5  | 출력 예시 : 2

# 풀이

from posixpath import split


n,k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기 - 반복문 이용 없이
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

##########################################################################################################

# <문제> 곱하기 혹은 더하기
# 첫째 줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어집니다.(1 <= S의 길이 <= 20)
# 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.
# 입력 예시1 : 02984 | 출력 예시1 : 576
# 입력 예시2 : 567   | 출력 예시2 : 210

# 풀이

# 문자열 S입력
data = input()

# 문자열의 첫번째를 숫자로 변경하여 결과값으로 대입
result = int(data[0])

for i in range(1,len(data)):
    # 두 수 중에서(현재와 다음 문자열) 하나라도 0 혹은 1인 경우, 곱하기말고 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)

##########################################################################################################

# <문제> 모험가 길드
# 첫째 줄에 모험가의 수 N이 주어집니다. (1 <= N <= 100000)
# 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
# 여행을 떠날 수 있는 그룹의 수의 최댓값을 출력합니다.
# 입력 예시 : 5 / 2 3 1 2 2  | 출력 예시 : 2

#풀이

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키키
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키키
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result) # 총 그룹의 수 출력

##########################################################################################################
# <문제> 상하좌우
# 첫째 줄에 공간의 크기를 나타내는 N이 주어집니다.(1 <= N <= 100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다.(1 <= 이동 횟수 <= 100)
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백을 기준으로 구분하여 출력합니다.
# 입력 예시 : 5 / R R R U D D   | 출력 예시 : 3 4

# 풀이

# n 입력
n = int(input())
x,y = 1,1 # 여행자 A 출발지점
plans = input().split()

# L,R,U,D에 따른 이동 방향 설정
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 continue
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 여행자 이동 수행
    x, y = nx, ny
# 최종 여행자 지점
print(x, y)

##########################################################################################################

# <문제> 시각
# 첫째 줄에 정수 N이 입력됩니다. (0 <= N < 23)
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력합니다.
# 입력 예시 : 5  | 출력 예시 : 11475

# 풀이

# 시간 입력
n = int(input())
count = 0 # 3이 포함되는 시간의 개수

for h in range(n + 1): # N+1 시간 동안
    for m in range(60): # 60분 
        for s in range(60): # 60초
            # 매 시각 안에 '3'이 포함되는 시간이 있다면 카운터 증가
            if '3' in str(h) + str(m) + str(s): 
                count += 1
print(count)

##########################################################################################################

# <문제> 왕실의 나이트
# 첫째 줄ㄹ에 8X8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이
# 입력된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.
# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
# 입력 예시 : a1 | 출력 예시 : 2

# 풀이

# 나이트의 위치 입력
input_data = input()
row = ord(input_data[0])-ord('a')+1 # 알파벳을 1-8로 바꾸기
column = int(input_data[1])

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    # 이동하고자 하는 위치 좌표
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

##########################################################################################################

# <문제> 문자열 재정렬
# 첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10000)
# 첫째 줄에 문제에서 요구하는 정답을 출력합니다.
# 입력 예시1 : K1KA5CB7 | 출력 예시1 : ABCKK13
# 입력 예시 2 : AJKDLSI412K4JSJ9D | 출력 예시2 : ADDIJJJKKLSS20

# 풀이

data = input()
result = []
sum = 0

# 문자열 하나씩 확인
for i in data:
    # 숫자일 경우 모두 더한 값을 도출
    if i.isdigit():
        sum += int(i)
    else:
        # 문자열일 경우 result에 삽입
        result.append(i)
# 문자열로 이루어진 리스트 오름차순으로 정렬
result.sort()
# 숫자가 하나라도 입력될 경우 가장 뒤에 삽입
if sum != 0:
    result.append(str(sum))
# 리스트를 문자열로 변환하여 주어진 형식으로 출력
print(''.join(result))