import random
nouns = ["Michael", "Girgis", "Brandon Cubero", "Willie Caulie-Stein",]
adjectives = ["gargantuan", "volomptuous", "quickly", "carelessly", "smelly", "green",]
verbs = ["Soloing the verse", "flossing", "rizzing",]
def wordPicker(list1, list2, list3):
    again = True
    while again == True:
        noun1 = random.choice(list1)
        noun2 = random.choice(list1)
        adjective1 = random.choice(list2)
        verb1 = random.choice(list3)
        verb2 = random.choice(list3)
        print(noun1," went to town", verb1, "on a", noun2, verb2, "a feather in his cap And called it", adjective1, "macaroni.")
        answer = input("Would you like to generate a new Mad Lib? ")
        if (answer == "no") or (answer == "No"):
            again = False
wordPicker(nouns, adjectives, verbs)