number = int(input("Input number here: "))
x = number

z = 2
def factor(y):
    for i in range(x):
        z = x % y
        if z == 0:
            print(y)
        y += 1
factor(1)
    
    
