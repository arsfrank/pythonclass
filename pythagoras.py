from math import sqrt
qwerty= input("Choose one, a,b,or c: ")
if qwerty== 'c':
            a = int(input("enter a: "))
            b = int(input("enter b: "))
            c = sqrt(a*a + b*b)
            print(c)
if qwerty== 'b':
            a = int(input("enter a: "))
            c = int(input("enter c: "))
            b = sqrt(c*c - a*a )
            print(b)
if qwerty== 'a':
            c = int(input("enter c: "))
            b = int(input("enter b: "))
            a = sqrt(c*c - b*b)
            print(a)



