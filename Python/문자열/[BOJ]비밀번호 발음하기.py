vowel = "aeiou"

while True:
    s = input()
    chk,chk2 = 0,0

    if s == "end": 
        break

    for i in s: # 모음 하나를 반드시 포함
        if i in vowel:
            chk2=1

    for i in range(1,len(s)): # 같은 글자 연속 X(ee,oo는 허용)
        if s[i] == s[i-1] and s[i] not in 'eo': 
            chk=1

    for i in range(len(s)-2): # 모음 자음이 3개 연속 X
        if s[i] in vowel and s[i+1] in vowel and s[i+2] in vowel: 
            chk=1

        elif s[i] not in vowel and s[i+1] not in vowel and s[i+2] not in vowel:
            chk=1

    if chk == 1 or chk2 == 0: 
        print("<" + s + "> is not acceptable." )
    else: 
        print("<" + s + "> is acceptable." )