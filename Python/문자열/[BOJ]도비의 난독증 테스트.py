while True:
    n = int(input())
    
    if n == 0: # 0이면 종료
        break
    
    result = []

    for i in range(n):
        s = input()
        result.append([s.lower(), s]) # 소문자로 변환 후 입력

    result.sort() # 소문자로 정렬

    print(result[0][1])