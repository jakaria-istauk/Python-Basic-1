from random import choice

questions =[]

while len(questions) < 3:
    new_q = input("Add a question: ")
    questions.append(new_q)

question = choice(questions)

answer = input(question+": ").lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh.... Okay")
