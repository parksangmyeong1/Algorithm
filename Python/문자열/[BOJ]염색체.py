import re

n = int(input())
regex = re.compile('^[A-F]?A+F+C+[A-F]?$')

for i in range(n):
    s = input()

    if regex.match(s):
        print('Infected!')
    else:
        print('Good')