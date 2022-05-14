import sys
input = sys.stdin.readline

a = int(input().rstrip())
t = int(input().rstrip())
want = int(input().rstrip())
count = 0
student = [i for i in range(a)]
st_cnt = 0 # 학생을 세기 위함
check = False # 이중문 break 용
n = 1
array = []

while True:
    n += 1
    array += [0, 1, 0, 1]
    
    for i in range(n):
        array.append(0)
    
    for i in range(n):
        array.append(1)
    
    for i in array:
        if i == want:
            count += 1

        st_cnt += 1   

        if count == t:
            check = True
            break

    if check:
        break

    array = []

print(student[st_cnt % a - 1])
