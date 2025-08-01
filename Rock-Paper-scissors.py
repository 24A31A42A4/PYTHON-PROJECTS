import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """  
 __________
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock, paper, scissors]
choices = ["rock", "paper", "scissors"]

computer_score = 0
user_score = 0

print("Game contains 3 rounds:")

for i in range(3):
    print(f"\n--- Round {i+1} ---")
    user_input = input("Enter rock, paper, or scissors: ").lower()

    if user_input not in choices:
        print("Invalid input! You lose this round.")
        computer_score += 1
        continue

    user_choice = choices.index(user_input)
    computer_choice = random.randint(0, 2)

    print("Your choice:")
    print(images[user_choice])
    print("Computer's choice:")
    print(images[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("User win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print("\n--- Final Result ---")
if user_score > computer_score:
    print(f"🎉 User win the game with score {user_score} - {computer_score}")
elif user_score < computer_score:
    print(f"💻 Computer wins the game with score {computer_score} - {user_score}")
else:
    print("🤝 The game is a tie!")
