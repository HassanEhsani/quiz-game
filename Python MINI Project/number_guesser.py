import random

top_of_rang = input("type a number: ")

if top_of_rang.isdigit():
    top_of_rang = int(top_of_rang)
    if top_of_rang <= 0:
        print("please type a number larger than 0 next time! ")
        quit()
else:
    print("please type a number next time! ")
    quit()
random_number = random.randint(0, top_of_rang)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please type a number next time! ")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")
print("You got it in", guesses, "guesses")
