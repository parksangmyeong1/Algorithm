n , k = map(int, input().split())
count = 0 # k번째 인덱스를 위해
check  = [False] * (n + 1) # 소수인지 체킹용

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if not check[j]:
            check[j] = True 
            count += 1

            if count == k:
                print(j)
                break