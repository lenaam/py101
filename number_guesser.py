import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range =int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 next time!")
        quit()
else:
    print('please type a number next time :)')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time :)')
        continue
    
    if user_guess == random_number:
        print("You got it !!")
        break
    else:
        if user_guess > random_number:
            print(" too close,you were above the number!")
        else:
            print("you were below the number")
#print("you got it in "+ str(guesses) + " guesses")
print(" you got it in", guesses, "guesses")
"""
randomrange : will not consider the last item, 
while randint(0, 1) returns a choice inclusive of the last item
"""


"""
isdigit :Check if all the characters in the text are digits,
method returns True if all the characters are digits, otherwise False

top_of_range =int(top_of_range)
and the value it taken from user is a string so we need to conver it to int
"""
