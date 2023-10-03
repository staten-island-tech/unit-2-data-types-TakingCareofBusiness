number1 = int(input("Input first number here "))
number2 = int(input("Input second number here "))
list1 = []
list2 = []
a = 1
def factor1(b):
    for i in range(number1):
        a = number1 % b
        if a == 0:
#0 is the remainder
            print(b)
        b += 1
factor1(1)

def factor2(b):
    for i in range(number2):
        a = number2 % b
        if a == 0:
#0 is the remainder
            print(b)
        b += 1
factor2(1)
c = 3
def factor3(b,d):
    for i in range(number1):
        a = number1 % b
        if a == 0:
            list1.append(b)
        b += 1
    for i in range(number2):
        c = number2 % d
        if c == 0:
            list2.append(d)
        d += 1
factor3(1,1)
maximum = 1
x = 0
def factor4(b,d):
    for i in range(number1):
        a = number1 % b
        if a == 0:
            list1.append(b)
        b += 1
    for i in range(number2):
        c = number2 % d
        if c == 0:
            list2.append(d)
        d += 1
    maximum = list1.max +list2.max
    for i in range(maximum):
        if (list1[x]) == (list2[x]):
            print((list1[x]))
    x += 1
factor4(1,1)
    
    