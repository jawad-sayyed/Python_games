import random
randNumber=random.randint(1,100)
userGuess=None
guesses=0
while(userGuess != randNumber):
    userGuess=int(input("Enter your guess: "))
    guesses += 1

    if(userGuess==randNumber):
      print("You guess is right")
    else:
        if(userGuess > randNumber):

            print("you guessed it wrong Enter a smaller number")

        else:
             print("You guess it wrong Enter a larger number")
print(f"You guesssed a number in {guesses} guesses")
try:
    with open("hiscore.txt", "r") as f:
        hiscore = int(f.read())
except FileNotFoundError:
        # If the file doesn't exist, set the hiscore to a very high number
    hiscore = float('inf')
except ValueError:
        # If the file is empty or contains invalid data, set the hiscore to a very high number
        hiscore = float('inf')

    # Check if the user has broken the high score
if guesses < hiscore:
    print("Congratulations! You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))















