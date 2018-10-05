films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        if age >= films[choice][0]:
            #check enough seats
            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry, We are sold out!")
                
        else:
            print("You are too young to see that film!")
    
    else:
        print("We don not have that film...")
