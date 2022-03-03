list = input()
m = 0
max = []
min = []

for ch in list:
    if ch == 'M':
        m += 1
    else:
        max.append((10**m)*5)
        
        if m == 0:
            min.append(5)
        else:
            min.append(10**m+5)

        m = 0
if m:
    for i in range(m):
        max.append(1)
        
    min.append(10**(m-1))
    
print(''.join(map(str, max)))
print(''.join(map(str, min)))