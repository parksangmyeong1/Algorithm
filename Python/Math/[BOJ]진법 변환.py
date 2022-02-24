import sys
input = sys.stdin.readline
n,b = input().split()

n = list(n) # list 역순으로 재정렬
n.reverse()

result = 0

for i in range(len(n)): # 리스트 길이만큼
    if not n[i].isdigit(): # 알파벳이면 숫자로 재정의
        result += (ord(n[i]) - 55) * (int(b)**i)

    else: 
        result += int(n[i]) * (int(b)**i)

print(result)