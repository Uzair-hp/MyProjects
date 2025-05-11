import random

print("This is Rock-Paper-Scissors!")

option = {1: "Rock", 2: "Paper", 3: "Scissor"}

def computer_choice():
    choice = random.choice(list(option.values()))
    print(f"Computer option: {choice}")
    return choice

while True:
    Player1 = input("Enter Your Option (Rock, Paper, Scissor) or 'exit' to quit: ").capitalize()
    
    if Player1 == "Exit":
        print("Thanks for playing!")
        break  # Ends the loop
    
    if Player1 not in option.values():
        print("Invalid Option. Please try again.")
        continue
    
    computer_option = computer_choice()

    if Player1 == computer_option:
        print("Tie!")
    elif (Player1 == "Rock" and computer_option == "Scissor") or \
         (Player1 == "Paper" and computer_option == "Rock") or \
         (Player1 == "Scissor" and computer_option == "Paper"):
        print("Winner: Player1 🎉")
    else:
        print("Winner: Computer 🤖")




    
    