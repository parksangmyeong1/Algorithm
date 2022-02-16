# DFS(Depth-First Search)
# DFS : 깊이 우선 탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 스택 자료구조(혹은 재귀 함수)를 이용
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리
#    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

# DFS 소스코드 예제

# DFS 메소드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9 # 8번 노드까지 있고 인덱스 0 사용하지 않기 위해 +1

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

##################################################################################################

# BFS(Breadth-First Search)
# BFS는 너비 우선 탐색이라고 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
# BFS는 큐 자료구조를 이용
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
#    모두 큐에 삽입하고 방문 처리
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

# BFS 소스코드 예제

from collections import deque

# BFS 메소드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end = ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9 # 8번 노드까지 있고 인덱스 0 사용하지 않기 위해 +1

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

##################################################################################################

# <문제> 음료수 얼려 먹기
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다.(1 <= N,M <= 1000)
# 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어집니다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
# 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.
# 입력 예시   | 출력 예시
# 4 5           3      
# 00110
# 00011
# 11111
# 00000

# 풀이

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

# N,M을 공백을 기준을 구분하여 입력 받기
n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기ㄴ
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1

print(result) # 정답 출력

##################################################################################################

# <문제> 미로탈출
# 첫째 줄에 두 정수 N,M(4<=N,M<=200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로
# 미로의 정보가 주어집니다. 각각의 수들은 공백없이 붙어서 입력으로 제시됩니다. 또한 시작칸과
# 마지막 칸은 항상 1입니다.
# 첫째 줄에 최소 이동 칸의 개수를 출력합니다.
# 입력예시   |   출력예시
# 5 6           10
# 101010 
# 111111 
# 000001 
# 111111 
# 111111 

# 풀이
# BFS 소스코드 구현
def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

from collections import deque

# N,M을 공백을 기준을 구분하여 입력 받기
n,m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# 이동할 4가지 방향 정의(상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# BFS를 수행한 결과 출력
print(bfs(0,0))