number1 = int(input("Input first number here "))
number2 = int(input("Input second number here "))
list1 = []
list2 = []
a = 1
c = 1
maximum = 1

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
    if (list1 and list2):
        print(max(list1 and list2))
factor4(1,1)
    