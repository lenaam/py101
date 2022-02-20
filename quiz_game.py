print("welocme to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print(" ok! lest pleay ;)")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1 
else:
    print("Incorrect")

answer = input("what does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1 
else:
    print("Incorrect")   

answer = input("what does RAM stand for? ")
if answer.lower() == "random access unit":
    print('Correct!')
    score += 1 
else:
    print("Incorrect")

answer = input("what does PSU stand for? ").lower()
if answer == "power supply unit":
    print('Correct!')
    score += 1 
else:
    print("Incorrect")    

answer = input("what is  the capital city of Saudi Arabia? ").lower()
if answer == "riyadh":
    print('Correct!')
    score += 4 
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct !!")
print("You got " + str((score / 4) * 100) + "%.")