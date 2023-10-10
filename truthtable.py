def weatherinput():
    weather = input("How's the weather outside? ")
    mood = input("Are you in the mood to walk your dog? ")
    dogmood = input("Is your dog in the mood to walk? ")
    if weather == "bad" or weather == "raining" or weather == "snowing" or weather == "hailing" or weather == "flooding" or weather == "hurricane" or weather == "tornado" or weather == "monsoon" or weather == "frightful":
        weather = False
    elif weather == "good" or weather == "sunny" or weather == "cloudy" or weather == "nice" or weather == "awesome" or weather == "epic" or weather == "awesome sauce" or weather =="pretty good":
        weather = True
    if mood == "yes" or mood == "yeah" or mood == "of course" or mood == "sure": 
        mood = True
    if mood == "no" or mood == "nope" or mood == "of course not" or mood == "not really" or mood == "nah":
        mood = False
    if dogmood == "yes" or dogmood == "yeah" or dogmood == "of course" or dogmood == "sure":
        dogmood = True
    if dogmood == "no" or dogmood == "nope" or dogmood == "of course not" or dogmood == "not really" or dogmood == "nah":
        dogmood = False
    if weather == True and mood == True and dogmood == True:
        print("You walked your dog!")
    elif weather == True and mood == True and dogmood == False:
        print("Your dog is lazy")
    if weather == True and mood == False and dogmood == True:
        print("Get over yourself and walk your dog")
    elif weather == False and mood == True and dogmood == True:
        print("You can't walk your dog :(")
    if weather == False and mood == False and dogmood == True:
        print("Lucky for you you can't walk your dog")
    elif weather == False and mood == True and dogmood == False:
        print("Lucky for your dog the weather is bad")
    if weather == True and mood == False and dogmood == False:
        print("You and your dog are lazy")
    elif weather == False and mood == False and dogmood == False:
        print("What a sad situation")
weatherinput()


