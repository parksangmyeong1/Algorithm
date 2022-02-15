#6001
print('Hello')

#6002
print('Hello World')

#6003
print('Hello')
print('World')

#6004
print("'Hello'")

#6005
print('''"Hello World"''')

#6006
print('"!@#$%^&*()\'')

#6007
print('''"C:\\Download\\\'hello'.py"''')

#6008
print('''print("Hello\\nWorld")''')

#6009
print(input())

#6010 #print(input())
print(int(input()))

#6011 #print(input())
print(float(input()))

#6012
a,b = input(),input()
print(a,b)

#6013
a,b = input(), input()
print('{b}\n{a}'.format(b=b, a=a))

#6014
a = float(input())
for i in range(3):
    print(a)

#6015
a, b = input().split()
print('{}\n{}'.format(int(a), int(b)))

#6016
a, b = input().split()
print('{} {}'.format(b, a))

#6017
a = input()
print(a,a,a)

#6018
print(a[0]+':'+a[1])

#6019
y,h,m = input().split('.')
print('{}-{}-{}'.format(m,h,y))

#6020
#1
print(''.join(input().split('-')))
#2
a,b = input().split('-')
print(a+b)

#6021
a = input()
for i in a:
    print(i)

#6022
a = input()
print(a[:2] + ' ' + a[2:4] + ' ' + a[4:])

#6023
a = input().split(':')
print(a[1])

#6024
a, b = input().split()
print(a + b)

#6025
a,b = map(int,input().split())
print(a+b)

#6026
a,b = float(input()),float(input())
print('{}'.format(a + b))

#6027
print('%x'%int(input()))

#6028
print('%X'%int(input()))

#6029
print('%o'%int(input(), 16))

#6030
print(ord(input()))

#6031
print(chr(int(input())))

#6032
print(-int(input()))

#6033
print(chr(ord(input())+1))

#6034
a,b = map(int,input().split())
print(a-b)

#6035
a,b = map(float,input().split())
print(a*b)

#6036
a = input().split()
for i in range(int(a[1])):
    print(a[0], end='')

#6037
n,s = int(input()),input()
for i in range(n):
    print(s, end='')

# 6038
#1 
a = list(map(int,input().split()))
print(a[0]**a[1])
#2
a, b = input().split()
print(int(a) ** int(b))

#6039
a, b = map(float,input().split())
print(a**b)

#6040
a, b = map(int,input().split())
print(a//b)

#6041
a, b = map(int,input().split())
print(a%b)

#6042
print(round(float(input()), 2))

#6043
a,b = map(float, input().split())
print('%0.3f' %(a/b))

#6044
a,b = map(int, input().split())
if a>=0 and b>0:
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(round(a/b,2))

#6045
a,b,c = map(int, input().split())
print(a+b+c, format((a+b+c)/3,".2f"))

#6046
a = int(input())
print(a<<1)

#6047
a,b = map(int,input().split())
print(a*(2**b))

#6048
a,b = map(int,input().split())
print(a<b)

#6049
a,b = map(int,input().split())
print(a==b)

#6050
a,b = map(int,input().split())
print(a<=b)

#6051
a,b = map(int,input().split())
print(a!=b)

#6052
print(bool(int(input())))

#6053
print(not bool(int(input())))

#6054
a, b = map(int,input().split())
print(bool(a and b))

#6055
a, b = map(int,input().split())
print(bool(a or b))

#6056
a, b = map(int,input().split())
print("True" if bool(a) != bool(b) else "False")

#6057
a, b = map(int,input().split())
print("True" if bool(a) == bool(b) else "False")

#6058
a, b = map(int,input().split())
print("True" if not (bool(a) or bool(b)) else "False")

#6059
print(~int(input()))

#6060
a,b = map(int, input().split())
print(a&b)

#6061
a,b = map(int, input().split())
print(a|b)

#6062
a,b = map(int, input().split())
print(a^b)

#6063
a,b = map(int, input().split())
print(a if a>b else b)

#6064
#1
a, b, c = map(int, input().split())
print((a if a < b else b) if (a if a < b else b) < c else c)
#2
print(min(list(map(int, input().split()))))

#6065
a = list(map(int, input().split()))
for i in a:
    if i%2==0:
        print(i)

#6066
a = list(map(int, input().split()))
for i in a:
    print("even" if i%2==0 else "odd")

#6067
a = int(input())
if a % 2 == 0 and a < 0:
    print('A')
elif a % 2 != 0 and a < 0:
    print('B')
elif a % 2 == 0 and a > 0:
    print('C')
elif a % 2 != 0 and a > 0:
    print('D')

#6068
score = int(input())
if score >= 90:
    print('A')
elif score >= 70:
    print('B')
elif score >= 40:
    print('C')
elif score >= 0:
    print('D')

#6069
grade = input()
if grade == 'A':
    print('best!!!')
elif grade == 'B':
    print('good!!')
elif grade == 'C':
    print('run!')
elif grade == 'D':
    print('slowly~')
else:
    print('what?')

#6070
month = int(input())
season = ''
if month in [12, 1, 2]:
    season = 'winter'
elif month in [3, 4, 5] :
    season = 'spring'
elif month in [6, 7, 8]:
    season = 'summer'
else:
    season = 'fall'
print(season)

#6071
while True:
    n = int(input())
    if n==0:
        break
    else:
        print(n)

#6072
n = int(input())
while n:
    print(n)
    n -= 1

#6073
n = int(input())
while n>0:
    n -= 1
    print(n)

#6074
a = input()
count = 0
while(count <= ord(a)-97):
    print(chr(97+count), end=' ')
    count += 1

#6075
a = int(input())
for i in range(a + 1):
    print(i)

#6076
a = int(input())
for i in range(a + 1):
    print(i)

#6077
num, sum = int(input()),0
for i in range(num + 1):
    if i%2==0: sum += i
print(sum)

#6078
c=''
while c!='q':
    c = input()
    print(c)

#6079
n = int(input())
i,sum = 0,0
while sum<n:
    i += 1
    sum += i
print(i)

#6080
n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        print(i+1, j+1)
    
#6081
n = input()
for i in range(1, 15 + 1):
	print('%X*%X=%X' %(int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))

#6082
n = int(input())
for i in range(1, n+1):
    if i%10==3 or i%10==6 or i%10==9: print('X', end=' ') 
    else: print(i, end=' ')

#6083
r,g,b = map(int,input().split())
c=0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)
            c += 1
print(c)

#6084
h,b,c,s = map(int,input().split())
print('%.1f MB' %((h * b * c * s / 8) / 1024 / 1024))

#6085
w,h,b = map(int,input().split())
print('%.2f MB' %((w*h*b / 8) / 1024 / 1024))

#6086
n = int(input())
i,sum = 0,0
while True:
    sum += i
    i += 1
    if sum>=n:
        break
print(sum)

#6087
n = int(input())
for i in range(1,n+1):
    if i%3!=0: print(i,end=' ')

#6088
a,d,n = map(int,input().split())
for i in range(n-1):
    a = a + d
print(a)

#6089
a,r,n = map(int,input().split())
for i in range(n-1):
    a = a * r
print(a)

#6090
a,m,d,n = map(int,input().split())
for i in range(n-1):
    a = a * m + d
print(a)

#6091
a, b, c = map(int, input().split())
day = 1
while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)

#6092
n = int(input())
nums = map(int, input().split())
temp = [0] * 23
for i in nums:
    temp[i-1] += 1
for i in temp:
    print(i, end=' ')

#6093
n = int(input())
nums = list(map(int, input().split()))
nums.reverse()
for i in nums:
    print(i, end=' ')

#6094
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[0])

#6095
n = int(input())
array = [[0] * 19 for _ in range(19)]
for i in range(n):
    x,y = map(int, input().split())
    if array[x-1][y-1]!=1:
        array[x-1][y-1]=1
for i in array:
    print(' '.join(map(str, i)))

#6096
array = []
for i in range(19):
    array.append([])
    k = input().split()
    for e in k:
        array[i].append(int(e))
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(19):
        array[a-1][j] = 1 if array[a-1][j] != 1 else 0
        array[j][b-1] = 1 if array[j][b-1] != 1 else 0
for i in array:
    print(' '.join(map(str, i)))

#6097
h,w = map(int, input().split())
array = [[0] * w for _ in range(h)]
n = int(input())
for i in range(n):
    l,d,x,y = map(int, input().split())
    for j in range(l):
        if d==0:
            array[x-1][y-1+j] = 1
        else:
            array[x-1+j][y-1] = 1
for i in array:
    print(' '.join(map(str,i)))

#6098
array = []
for i in range(10): 
    array.append(list(map(int, input().split())))
x, y = 1, 1
flag = True
while flag:
    if array[x][y] == 2:
        array[x][y] = 9
        flag = False
    elif array[x][y+1] == 1:
        array[x][y] = 9
        if array[x+1][y] == 1:
            flag = False
        else:
            x += 1
    else:
        array[x][y] = 9
        y += 1
for i in array:
    print(' '.join(map(str, i)))