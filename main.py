import functions as f

print("Welcome to the Number Guessing Game!")

# See getName function in functions.py
name = f.getName()

# Game plays until program is exited.
while True:
    # Plays main game and saves number of guesses
    totalGuesses = f.mainGame()

    # Checks to see if new high score is set and updates txt file if so.
    f.updateHighScores(name, totalGuesses)

    # Prints high scores after every game.
    f.printHighScores()
