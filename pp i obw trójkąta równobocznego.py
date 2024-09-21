import math 

print(math.sqrt(9))
print(math.pi)

inp = input()
if 'a' == inp:
    print('pp - a obw - b')
    inp = input('co liczę =')
    a = float(input('a = '))
    if inp == 'a':
        print((a**2*3**(1/2))/4)
    elif inp == 'b':
        print(3*a)