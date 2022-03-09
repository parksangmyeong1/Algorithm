import sys
input = sys.stdin.readline

while True:
    try: # try-excepy
        s, t = input().split()
        check = False
        index = 0

        for i in range(len(t)):
            if t[i] == s[index]:
                index += 1

                if index == len(s): # 입력한 문자열이 있으면 True
                    check = True
                    break
        if check:
            print('Yes')
        else:
            print('No')
    
    except: # 입력 더 없으면 while문 탈출
        break