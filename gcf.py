number1 = int(input("Input first number here "))
number2 = int(input("Input second number here "))
list1 = []
list2 = []
a = 1
c = 1
maximum = 1

def factor4(b,d,x):
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
    maximum = (max(list1)) +(max(list2))
    for i in range(maximum):
        if (list1[x]) == (list2[x]):
            print((list1[x]))
    x += 1
factor4(1,1,0)
    
    
