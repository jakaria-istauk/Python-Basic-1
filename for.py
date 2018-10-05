for number in range(1,10,2):
    print(number)


vowels = 0
consonants = 0
word = input("Give a string: ").lower()

for letter in word:
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter in ".?@#$&!":
        pass
    elif letter in "1234567890":
        pass
    else:
        consonants = consonants + 1
        


print("There is {} vowels".format(vowels))
print("There is {} consonants".format(consonants))
