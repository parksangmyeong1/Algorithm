duck = list(input())
quack = 'quack'
idx = 0
answer = 0
visited = [False] * len(duck)
first = False

if len(duck) % 5 != 0 or duck[0] != "q": # 제외 조건
    print(-1)
    exit()

for a in range(len(duck)):
    if duck[a] == "q" and not visited[a]:  # 방문하지 않았고, q인 곳 -> 시작 구간이다.
        first = True

        for i in range(len(duck)):
            if not visited[i] and quack[idx] == duck[i]:
                visited[i] = True

                if duck[i] == "k":
                    if first:
                        answer += 1
                        first = False

                    idx=0
                    continue

                idx += 1

if answer == 0 or not all(visited):
    print(-1)
else:
    print(answer)

#####################################
# 다시 한번 풀어보기