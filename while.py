number = 0

while number <=20:
    if number % 2 == 0:
        print(number)
    number= number + 1


l = []

while len(l) < 3:
    name = input("Add a new name: ").strip().capitalize()
    l.append(name)

print("Sorry !! List is full")
print(l)

        
