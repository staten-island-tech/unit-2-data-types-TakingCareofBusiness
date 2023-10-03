number1 = int(input("Input first number here "))
number2 = int(input("Input second number here "))

a = 1
def factor1(b):
    for i in range(number1):
        a = number1 % b
        if a == 0:
#0 is the remainder
            print(b)
        b += 1
factor1(1)
c = 3
def factor2(d):
    for i in range(number2):
        c = number2 % d
        if c == 0:
#0 is the remainder
            print(d)
        d += 1
factor2(1)
    