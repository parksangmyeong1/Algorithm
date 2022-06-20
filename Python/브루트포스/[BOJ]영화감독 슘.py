import sys
input = sys.stdin.readline

n = int(input().rstrip())

i = 0
count = 0

while True:
    if '666' in str(i):
        count += 1
    
    if count == n:
        break
    
    i += 1
    
print(i)