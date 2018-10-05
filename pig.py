#get sentence from user

orginal = input("Please enter a sentence: ").strip().lower()

#split sentence into word

words = orginal.split()



#loop through words and convert to pig latin

new_words = []

for word in words:
    #if strat with vowel just start add "yay"
    if word[0] in "aeiou":
        new_word = word+"yay"
        new_words.append(new_word)
    else:
        #Otherwise, move the fisrt consonat cluser to ens adn add "ay"
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)



#stick words back together

output = " ".join(new_words)

#output final string

print(output)
