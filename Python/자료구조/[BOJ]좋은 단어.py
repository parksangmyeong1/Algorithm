import sys
input = sys.stdin.readline
 
n = int(input())
count = 0
 
for i in range(n):
    s = input().rstrip()
    stack = []
 
    for j in range(len(s)):
        if stack and s[j] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[j])
 
    if not stack:
        count += 1

print(count)