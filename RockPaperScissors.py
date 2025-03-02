import random
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()
        if player == "rock":
            playerText = player + " 🪨"
        elif player == "paper":
            playerText = player + " 📜"
        elif player == "scissors":
            playerText = player + " ✂️"
        if computer == "rock":
            computerText = computer + " 🪨"
        elif computer == "paper":
            computerText = computer + " 📜"
        elif computer == "scissors":
            computerText = computer + " ✂️"

    print("Computer: ", computerText)
    print("Player: ", playerText)

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "paper":
        print("Computer won! ❌")
    elif player == "rock" and computer == "scissors":
        print("Player won! ✅")
    elif player == "paper" and computer == "rock":
        print("Player won! ✅")
    elif player == "paper" and computer == "scissors":
        print("Computer won! ❌")
    elif player == "scissors" and computer == "rock":
        print("Computer won! ❌")
    elif player == "scissors" and computer == "paper":
        print("Player won! ✅")

    playAgain = input("Would you like to play again? (y/n): ").lower()
    if playAgain != 'y':
        break
print("Bye!")