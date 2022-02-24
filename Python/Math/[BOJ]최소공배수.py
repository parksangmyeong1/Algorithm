import math # math 함수 이용
t = int(input())

for i in range(t):
    a,b = map(int, input().split())

    print(math.lcm(a,b))

##################################################################

t = int(input())

def gcd(x,y): # 최대 공약수
    if x == 0:
        return y
    return gcd(y%x, x)

def lcm(x,y): # 최소 공배수
    return x*y//gcd(x,y)

for i in range(t):
    a,b = map(int, input().split())

    print(lcm(a,b))