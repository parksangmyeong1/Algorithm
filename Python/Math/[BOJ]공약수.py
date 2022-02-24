import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b): # 최대 공약수
    if(a == 0):
        return b

    return gcd(b % a, a)

g = gcd(arr[0], gcd(arr[1], arr[-1]))

for i in range(1, (g // 2) + 1): # 반복문 이용해서 공약수 모두 출력
    if g % i == 0:
        print(i)

print(g)