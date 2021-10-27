import random
while True:
    choices=["rock","paper","scissors"]

    computer= random.choice(choices)
    player= None

    while player not in choices:
        player=input("rock, paper, scissors?").lower()

    if player== computer:
        print("computer: ", computer)
        print("player:", player)
        print("Tie!")
    elif player=="scissors" :
        print("computer: ", computer)
        print("player:", player)
        if computer=="rock":
            print("Lose!")
        else:
            print("Win!")
    elif player=="rock" :
        print("computer: ", computer)
        print("player:", player)
        if computer=="paper":
            print("Lose!")
        else:
            print("Win!")
    else :
        print("computer: ", computer)
        print("player:", player)
        if computer=="scissors":
            print("Lose!")
        else:
            print("Win!")
    play_again= input("Play again? Yes/no").lower()
    if play_again!="yes":
        break
print("Bye")