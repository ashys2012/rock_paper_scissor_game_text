# text based rock paper scissor game
# bigginer project


i = 0       

while i < 10:       

    user_choice = input("Choose rock, paper or scissor\n")

    if user_choice in ("Rock", "rock", "ROCK", "r", "R"):
        user_choice = "rock"

    elif user_choice in ("Paper", "paper", "PAPER", "p", "P"):
        user_choice = "paper"

    elif user_choice in ("Scissor", "scissor", "SCISSOR", "s", "S"):
        user_choice = "scissor"
    else:
        print("invalid option")
        break

    import random

    characters = ['rock', 'paper', 'scissor']
    z = random.choice(characters)
    print(z)

    if user_choice == 'rock' and z == 'paper':
        print("Computer wins")

    elif user_choice == 'rock' and z == 'scissor':
        print("Player wins")

    elif user_choice == 'paper' and z == 'rock':
        print("Player wins")

    elif user_choice == 'paper' and z == 'scissor':
        print("Computer wins")

    elif user_choice == 'scissor' and z == 'rock':
        print("Computer wins")

    elif user_choice == 'scissor' and z == 'paper':
        print("Player wins")

    else:
        print("Tie Game")










