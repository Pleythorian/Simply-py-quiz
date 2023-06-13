print("Welcome")

playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()

print("Okay, Lets Play!")

answer = input("What is the founder of Tesla's name? ")
if answer.lower() == "Elon Musk":
    print("Correct")
else:
    print("Incorrect")

answer = input("What is the first letter in the word play? ")
if answer.lower() == "p":
    print("Correct")
else:
    print("Incorrect")

answer = input("What is 19+200? ")
if answer.lower() == "219":
    print("Correct")
else:
    print("Incorrect")

answer = input("What letter comes after a? ")
if answer.lower() == "b":
    print("Correct")
else:
    print("Incorrect")

answer = input("What is 6+100? ")
if answer.lower() == "106":
    print("Correct")
else:
    print("Incorrect")
