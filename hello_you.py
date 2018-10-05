#Ask user for name

name = input("What is your name?: ")

#Ask user for age

age = input("How Old are you?: ")


#Ask user for city

city = input("Where do you live?: ")


#Ask user what they enjoy

enjoy = input("What do you love doing?: ")

#Creat output text

string = "Your Name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, enjoy)
print(output)

#Print output to screen

