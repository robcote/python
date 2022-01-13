print("Welcome to my Quiz!")

playing = input("Are you ready to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's begin!" )
score = 0

answer = input("What is the capital of Kentucky? ")
if answer.lower() == "frankfort":
    print('Correct!')
    score += 1
else:
    print("Incorrect.")

answer_1 = input("What is the largest city in Kentucky? ")
if answer_1.lower() == "louisville":
    print('Correct!')
    score += 1
else:
    print("Incorrect.")

answer_2 = input("What is the state bird of Kentucky? ")
if answer_2.lower() == "cardinal":
    print('Correct!')
    score += 1
else:
    print("Incorrect.")

answer_3 = input("What is the state flower of Kentucky? ")
if answer_3.lower() == "goldenrod":
    print('Correct!')
    score += 1
else:
    print("Incorrect.")

answer_4 = input("What is the state song of Kentucky? ")
if answer_4.lower() == "my old kentucky home":
    print('Correct!')
    score += 1
else:
    print("Incorrect.")

print("You got " + str(score) + " questions correct!")
print( str((score) / 5 * 100) + " %")
