import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock, paper, scissors]

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, or 3 to quit.\n"))

    if user_choice == 3:
        print("You chose to quit.")
        break

    print(f"You chose: {game_images[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {game_images[computer_choice]}")

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number. You lose!")
    else:
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == 0 and computer_choice == 2) or \
             (user_choice == 1 and computer_choice == 0) or \
             (user_choice == 2 and computer_choice == 1):
            print("You win!")
        else:
            print("Computer wins!")