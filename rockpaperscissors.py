"""
AUEB Excercise chapter 4. Advanced Python

Develop a rock paper scissors game.

Author: Kountouris Panagiotis

Date: May 05 2023

"""

import random

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

# Declaring the logo
logo = """\033[34m
_________            .___.__                 ___________              __                       
\_   ___ \  ____   __| _/|__| ____    ____   \_   _____/____    _____/  |_  ___________ ___.__.
/    \  \/ /  _ \ / __ | |  |/    \  / ___\   |    __) \__  \ _/ ___\   __\/  _ \_  __ <   |  |
\     \___(  <_> ) /_/ | |  |   |  \/ /_/  >  |     \   / __ \\  \___|  | (  <_> )  | \/\___  |
 \______  /\____/\____ | |__|___|  /\___  /   \___  /  (____  /\___  >__|  \____/|__|   / ____|
        \/            \/         \//_____/        \/        \/     \/                   \/     
__________               __            __________                                        _________      .__                                  
\______   \ ____   ____ |  | __        \______   \_____  ______   ___________           /   _____/ ____ |__| ______ _________________  ______
 |       _//  _ \_/ ___\|  |/ /  ______ |     ___/\__  \ \____ \_/ __ \_  __ \  ______  \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 |    |   (  <_> )  \___|    <  /_____/ |    |     / __ \|  |_> >  ___/|  | \/ /_____/  /        \  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
 |____|_  /\____/ \___  >__|_ \         |____|    (____  /   __/ \___  >__|            /_______  /\___  >__/____  >____  >____/|__|  /____  >
        \/            \/     \/                        \/|__|        \/                        \/     \/        \/     \/                 \/ 
\033[0m"""

print(logo)

while True:
    # Get input and randomize in order to compare. Convert to lowercase. Print with nice colors. :)
    player_input = input("Enter your choice(\033[32mrock/paper/scissors\033[0m) or '\033[31mquit\033[0m' to exit: ").lower()

    # Player selected to quit
    if player_input == "quit": break

    # Check if player_input is valid
    if player_input not in options: 
        print("Invalid input. Try again.")
        continue

    # Randomize computer choice
    computer_str = random.choice(options)

    # Printing the player and the computer choice on console. With nice colors d(^_^)b 
    print(f"You chose: \033[32m{player_input}\033[0m")
    print(f"Computer chose: \033[34m{computer_str}\033[0m")

    # Compare the player and the computer choice and print the result
    if player_input == computer_str:
        print("It's a tie!")
        continue
    elif player_input == "rock" and computer_str == "scissors":
        print("You win!")
        player_score += 1
        continue
    elif player_input == "paper" and computer_str == "rock":
        print("You win!")
        player_score += 1
        continue
    elif player_input == "scissors" and computer_str == "paper":
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1
        continue

print("-----------------------------------------------------")
print(f"Final score. You: [\033[32m{player_score}\033[0m] , Computer: [\033[34m{computer_score}\033[0m]")
print("Thank you for playing !!")

    