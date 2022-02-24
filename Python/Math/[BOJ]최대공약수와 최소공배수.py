import math

x,y = map(int, input().split())

print(math.gcd(x,y)) # math 함수 이용
print(math.lcm(x,y))

##################################################################

x,y = map(int, input().split())

def gcd(x,y): # 최대 공약수
    if x == 0:
        return y
    return gcd(y%x, x)

def lcm(x,y): # 최소 공배수
    return x*y//gcd(x,y)

print(gcd(x,y))
print(lcm(x,y))