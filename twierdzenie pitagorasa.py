import math 


a = float(input())
b = float(input())
c = float(input())
if a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2:
    print('to jest tr prostokątny')
else:
    print('to nie jest tr prostokątny')