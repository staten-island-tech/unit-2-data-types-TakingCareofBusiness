number1 = int(input("Input first number here "))
number2 = int(input("Input second number here "))
list1 = []
list2 = []
list3 = []
a = 1
c = 1
maximum = 1
e = 1
g = 1

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
    
    if (max(list1)) > (max(list2)):
        maximum = (max(list1))
    if (max(list1)) < (max(list2)):
        maximum = (max(list2))
    print(list1)
    print(list2)
    print(maximum)
    for i in range(maximum):
        if (list1[x]) == (list2[x]) or (list2[x]) == (list1[x]):
           print(list2[x])
           list3.append(x + 1)
        if (not(list1[x]) == (list2[x])):
            g = 1
            e = x + g
            for i in range(e):
                if  (list1[e]) == (list2[e]):
                    g += 0
                if (not(list1[e]) == (list2[e])):
                    g += 1
        x += 1
    print(list3)
factor4(1,1,-1)
    
    
