import random

print("LETS PLAY A GUESSING GAME")

nummm = random.randint(1,9)

chances = 0

print("GUESS ANY NUMBER BETWEEN 1 To 9")


while chances<5:
    guess = int(input("ENTER YOUR GUESS "))

    if guess == nummm:
        print("CORRECT!")
        break

    elif guess < nummm:
        print("YOUR GUES IS LOW! PLEASE THINK OF A HIGHER NUMBER!")
        print("GUESS A NUMBER HIGHER THAN THIS")

    else:
        print("YOUR GUESS IS  HIGH. PLEASE THINK OF A LOWER NUMBER!")
        print("GUESS A NUMBER LESSER THAN THIS")

    chances+=1

if chances==5 and guess!= nummm:
    print("YOU LOSE")
