known_users = ["Jakaria", "Parvez", "Pritom", "Shantoo", "Golu", "Shahin", "Akib"]

print(known_users)

while True:
    print("Hi ! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system(y/n): ").lower()

        if remove == "y":
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem, I didn't want to leave you to anway!")

            
    else:
        print("Hmmm! I don't think i have met you yet {}.".format(name))
        add = input("Would you like to be added to the system(y/n): ").lower()
        if add == "y":
            known_users.append(name)
            print(known_users)
        elif add == "n":
            print("No problem, See you again!")
            

        
