import random

# List of lower case quit commands to test input against
quitCommands = {"q", "quit"}

# Function to read high score text file and return list with information from file
def loadHighScores():
    highScoreList = list()

    with open("topPlayers.txt", "r") as file:
        for line in file:
            highScoreList.append([int(line[0:10]), line[10:].rstrip()])

    return highScoreList

# Reads high score using loadHighScore command and prints nice display
def printHighScores():
    highScoreList = loadHighScores()
    print("***** HIGH SCORES *****")
    print("AGE".ljust(10) + "NAME")
    for entry in highScoreList:
        print(str(entry[0]).ljust(10) + entry[1])
    print()

# Exits game. Always prints high score.
def quitter():
    print("WHY DON'T YOU WANT TO PLAY WITH ME?")
    printHighScores()
    exit()

# Function to ask player to input name. Forces name to be 25 characters or less. Error catching for ctrl-D
# and unexpected exception
def getName():
    try:
        name = input("What is your name?\n")
        if name.lower() in quitCommands:
            quitter()
        elif len(name) > 25:
            print("Name too long: first 25 characters used.")
            return name[0:25]
        else:
            return name
    except EOFError:
        print("Termination command detected from user.")
        quitter()
    except Exception as e:
        print(f"Unexpected exception: {e}. Quitting for safety.")
        exit()


# Defines a function to return singular for 1 and plural for more than 1
def guessSoFar(num):
    if num == 1:
        return "1 guess"
    elif num > 1:
        return f"{num} guesses"


# mainGame function to play game. Note function returns output: the total number of guesses
def mainGame():

    # Note random.randint is inclusive for both lower and upper endpoint
    # See: https://docs.python.org/3/library/random.html
    correctNum = random.randint(1, 100)

    # Initializes the current guess and the number of guesses so far at 0
    guess = 0
    numGuesses = 0

    # Creates loop that ends when the current guess is determined to be correct
    while guess != correctNum:
        try:

            # Accepts input for guess. First checks for quit command and exits program if quit
            # Detected. Otherwise attempts to convert guess to an int.
            guess = input("Guess a number from 1 to 100, or type QUIT to exit.\n")
            if guess.lower() in quitCommands:
                quitter()
            else:
                guess = int(guess)

            # Raises a ValueError if "guess" is not in the proper range.
            # Technically this catches both Value and Type errors.
            if guess not in range(1, 101):
                raise ValueError
            # If no quit command was entered and the guess was legal, number of
            # guesses will iterate by one.
            else:
                numGuesses = numGuesses + 1

            # Tells user guess was either too high or too low
            # Also prints number of guesses so far
            if guess < correctNum:
                print(f"That guess was too low! {guessSoFar(numGuesses)} so far!")
            elif guess > correctNum:
                print(f"That guess was too high! {guessSoFar(numGuesses)} so far!")

        # Error message sent when ValueError is raised from in While loop above
        except ValueError:
            print("A whole number between 1 and 100, please.")
        except EOFError:
            print("Termination command detected from user.")
            quitter()
        except Exception as e:
            print(f"Unexpected exception: {e}. Quitting for safety.")
            exit()

    # Prints victory message with number of guesses if while loop terminates
    # (That is, if the guess is correct)
    print(f"YOU WIN!!! {guess} was the correct answer! It took you {guessSoFar(numGuesses)}!")
    print()
    return numGuesses


# Checks if a given number of totalGuesses is low enough to push someone off high score list. If so, prints
# message, and writes over old txt file.
def updateHighScores(name, totalGuesses):
    highScoreList = loadHighScores()
    if totalGuesses < highScoreList[4][0]:
        print("YOU GOT A HIGH SCORE!!!")
        del highScoreList[-1]
        highScoreList.append([totalGuesses, name])
        highScoreList.sort(key=lambda entry:entry[0])
        with open("topPlayers.txt", "w") as file:
            for entry in highScoreList:
                file.write(str(entry[0]).ljust(10) + entry[1] + "\n")

    # Otherwise prints encouraging message and returns original high score list
    else:
        print("You didn't make the high score list. Try Again!")
