while True:
    password = input()
    
    if password == 'END':
        break
    else:
        print(password[::-1])