money = int(input())
stocks = list(map(int, input().split()))

def jun(j_money):
    j_stock = 0

    for stock in stocks:
        j_stock += j_money // stock
        j_money = j_money % stock

        if j_money == 0:
            break
        
    return j_money, j_stock

def sung(s_money):
    down = 0
    up = 0
    s_stock = 0

    for i in range(1,14):
        if stocks[i-1] > stocks[i]:
            down += 1
            up = 0
        elif stocks[i-1] < stocks[i]:
            down = 0
            up += 1
        else:
            down = 0
            up = 0
        
        if stocks[i] <= s_money and down >= 3:
            s_stock += s_money // stocks[i]
            s_money = s_money % stocks[i]
    
    return s_money, s_stock

j_money, j_stock = jun(money)
s_money, s_stock = sung(money)
j_total = j_money + j_stock * stocks[-1]
s_total = s_money + s_stock * stocks[-1]

if j_total > s_total:
    print('BNP')
elif j_total < s_total:
    print('TIMING')
else:
    print('SAMESAME')