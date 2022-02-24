a,b,c,m = map(int, input().split())
tired = 0 # 피로도
work = 0 # 일

if a > m : # 예외 케이스 : 처음부터 증가하는 피로도가 max피로도 넘을 경우
    print(0)

else:
    for i in range(1,25): # 24시간 동안
        if m >= (tired + a): # max 피로도를 넘지 않아서
            tired += a # 피로도 증가
            work += b # 일한 만큼 증가

        else: # max 피로도를 넘어서
            tired -= c # 쉬었을 경우, 피로도 감소

            if tired < 0: # 조건 : 피로도가 음수면 0으로 입력
                tired = 0

    print(work)