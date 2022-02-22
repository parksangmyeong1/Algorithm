arr = list(input())

result = 0
tmp = 1
stack = []

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
        tmp *= 2
    
    elif arr[i] == '[':
        stack.append(arr[i])
        tmp *= 3
    
    elif arr[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        
        if arr[i-1] == '(':
            result += tmp
        
        stack.pop()
        tmp //= 2
    
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        
        if arr[i-1] == '[':
            result += tmp
        
        stack.pop()
        tmp //= 3

if stack:
    print(0)
    
else:
    print(result)