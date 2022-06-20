import sys
input = sys.stdin.readline

t = int(input().rstrip())

arr = []
result = 0
answers = []

for i in range(t):
    n = int(input().rstrip())
    
    start = list(input().rstrip())
    goal = list(input().rstrip())

    for i in range(n):
        if start[i] != goal[i]:
            arr.append(start[i])
    
    if arr.count("B") >= arr.count("W"):
        result = arr.count("B")
    else:
        result = arr.count("W")
        
    answers.append(result)
    arr = []

for answer in answers:
    print(answer)