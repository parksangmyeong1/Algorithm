import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

array = []
count = 0
result = ''

for i in range(n):
    array.append(list(map(str, input().rstrip())))

for i in range(m):
    a,c,g,t, = 0,0,0,0

    for j in range(n):
        if array[j][i] == 'A':
            a += 1
        elif array[j][i] == 'C':
            c += 1
        elif array[j][i] == 'G':
            g += 1
        elif array[j][i] == 'T':
            t += 1
    
    if max(a,c,g,t) == a:
        result += 'A'
        count += c + g + t

    elif max(a,c,g,t) == c:
        result += 'C'
        count += a + g + t

    elif max(a,c,g,t) == g:
        result += 'G'
        count += a + c + t

    elif max(a,c,g,t) == t:
        result += 'T'
        count += a + c + g

print(result)
print(count)