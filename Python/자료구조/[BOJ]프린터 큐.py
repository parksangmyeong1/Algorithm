from collections import deque

t = int(input()) # 테스트 케이스 입력

for i in range(t):
    n,m = list(map(int, input().split())) # n,m 입력
    imp = list(map(int, input().split())) # 중요도 리스트 입력
    q1 = deque() # 중요도 큐
    q2 = deque() # 인덱스 큐
    count = 1 # 결과값
    
    for j in range(len(imp)): # 큐에 중요도 리스트와 인덱스 리스트 삽입
        q1.append(imp[j])
        q2.append(j)

    while True:
        if q1[0] == max(q1): # 첫번째 중요도가 최고면
            if q2[0] == m: # 첫번째 중요도가 찾는 인쇄지점이면 출력
                print(count)
                break
            
            else: # 찾는 지점이 아니면 다음 검사
                q1.popleft()
                q2.popleft()
                count += 1
        
        else: # 리스트 << 방향으로 하나씩 당기기
            q1.rotate(-1)
            q2.rotate(-1)