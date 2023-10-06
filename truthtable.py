weather = input("How's the weather outside? ")
mood = input("Are you in the mood to walk your dog? ")
dogmood = input("Is your dog in the mood to walk? ")

def weatherinput():
    if weather == "bad" or "raining" or "snowing" or "hailing" or "flooding" or "hurricane" or "tornado" or "monsoon":
        weather = False
    elif weather == "good" or "sunny" or "cloudy" or "nice" or "awesome" or "epic" or "awesome sauce":
        weather = True
    else:
        print("Error")
    if mood == "yes" or "yeah" or "of course" or "sure": 
        mood = True
    if mood == "no" or "nope" or "of course not" or "not really" or "nah":
        mood = False
    else:
        print("Error")
    if dogmood == "yes" or "yeah" or "of course" or "sure":
        dogmood = True
    if dogmood == "no" or "nope" or "of course not" or "not really" or "nah":
        dogmood = False
    else:
        print("Error")
    if weather == True and mood == True and dogmood == True:
        print("You walked your dog!")
    if weather == True and mood == True and dogmood == False:
        print("Your dog is lazy")
    if weather == True and mood == False and dogmood == True:
        print("Get over yourself and walk your dog")
    if weather == False and mood == True and dogmood == True:
        print("You can't walk your dog :(")
    


