import sys
input = sys.stdin.readline

def is_palidrome(str): # 회문 구하는 함수
    left_false = False
    right_false = False

    for i in range(len(str)//2):
        if str[i] != str[len(str)-1-i]: 
            for j in range(i, len(str)//2): # 왼쪽에서 앞 글자 삭제 후 비교
                if str[j+1] != str[len(str)-1-j]: 
                    left_false = True

            for j in range(i, len(str)//2): # 오른쪽에서 뒤 글자 삭제 후 비교
                if str[j] != str[len(str)-1-j-1]: 
                    right_false = True

            if left_false and right_false: # 둘 다 True면 2
                return 2
            
            # elif left_false or right_false: 가 아니라 esle 인 이유
            # aabcbcaa 같은 경우 left, right 둘다 False가 나옴
            # 그러나 유사 회문이라서 1이 나와야함 따라서 elif 말고 else로 수정
            else: # 유사 회문이면 1 
                return 1
                
    return 0 # 회문이면 0

t = int(input())

for i in range(t):
    s = input().rstrip() # rstrip()를 쓰지 않으면 \n도 문자열에 추가됨
    print(is_palidrome(s))
