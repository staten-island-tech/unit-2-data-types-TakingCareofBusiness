number1 = int(input("Input first number here "))
number2 = int(input("Input second number here "))
list1 = []
list2 = []
list3 = []
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
    print(list1)
    print(list2)
    if (max(list1)) > (max(list2)):
        maximum = (max(list1))
    elif (max(list1)) < (max(list2)):
        maximum = (max(list2))
    for i in range(maximum):
        if (list1[i]) == (list2[i]):
            list3.append(list1[i])
        elif not((list1[i]) == (list2[i])):
            
            print(max(list3))
factor4(1,1)
    
