#set stopwatch
#if current time has 5 in a minute spot eastward false westward true
#if current time has 0 in the minute spot eastward true westward false



x = 1123
y = False
def truthy(x,y):
    if type(x) != bool or type(y) != bool:
        type ("Glitch")
    else:
        if x == y:
            print("false")
        elif x != y:
            print("true")
truthy(x,y)