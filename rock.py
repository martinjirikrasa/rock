import random

# set optiones for game
options = ["rock", "paper", "scissors"]

# set user and computer score to 0
user_score = 0
comp_score = 0

# get users input for how many games ypou want to play
win = int(input("Set how many wins are enought to win the game: "))

while (user_score < win) or (comp_score < win):

    # keep getting users input for his choice and generate computers input
    user_input = input("Type rock, paper, scissors: ")
    comp = random.choice(options)


    if user_input == "rock":
        if comp == "rock":
            print("\ntie!\n")

    elif user_input == "paper":
        if comp == "paper":
            print("\ntie!\n")

    elif user_input == "scissors":
        if comp == "scissors":
            print("\ntie!\n")
    # user rock
    if (user_input == "rock") & (comp == "paper"):
        comp_score += 1
        print("\nyou lost!\n")
        print("User: {} Computer: {}".format(user_score, comp_score))

    if (user_input == "rock") & (comp == "scissors"):
        user_score += 1
        print("\nyou win!\n")
        print("User: {} Computer: {}".format(user_score, comp_score))
    # user paper
    if (user_input == "paper") & (comp == "rock"):
        user_score += 1
        print("\nyou won!\n")
        print("User: {} Computer: {}".format(user_score, comp_score))

    if (user_input == "paper") & (comp == "scissors"):
        comp_score += 1
        print("\nyou lost!\n")
        print("User: {} Computer: {}".format(user_score, comp_score))
    # user scissors
    if (user_input == "scissors") & (comp == "paper"):
        user_score += 1
        print("\nyou win!\n")
        print("User: {} Computer: {}".format(user_score, comp_score))

    if (user_input == "scissors") & (comp == "rock"):
        comp_score += 1
        print("\nyou lost!\n")
        print("User: {} Computer: {}".format(user_score, comp_score))

    # end the game after n games
    if user_score == win:
        print("Congratulations, You have won the game!")
        break
    if comp_score == win:
        print("You Lost the game, computer beat you..")
        break


