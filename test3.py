number1 = int(input("Input number here "))
number2 = int(input("Input number here "))
list1 = []

number = 1
def factor():
    if number1 > number2:
        number = number1
    elif number1 < number2:
        number = number2
    for i in range(1, number+1):
        if number1 % i == 0 and number2 % i == 0:
            list1.append(i)
    print(max(list1))
  
factor()

