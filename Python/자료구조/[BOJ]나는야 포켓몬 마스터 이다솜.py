import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

dict = {}

for num in range(1, n+1):
    word = input().rstrip() # 개행문자 제거 위함
    dict[num] = word
    dict[word] = num

for i in range(m):
    test = input().rstrip()
    
    if test.isdigit():
        print(dict[int(test)])
        
    else:
        print(dict[test])