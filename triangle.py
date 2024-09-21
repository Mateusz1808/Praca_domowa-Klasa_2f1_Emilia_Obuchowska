import math 


a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    print("to jest tr")
else:
    print("to nie jest tr")

a = float(input())
b = float(input())
c = float(input())
if a + b > c:
    if b + c > a: 
        if a + c > b:
            print("to jest tr")
        else:
            print("to nie jest tr")
    else:
        print("to nie jest tr")
else:
    print("to nie jest tr")