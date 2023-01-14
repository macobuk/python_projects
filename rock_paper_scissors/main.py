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

weapons = [rock,paper,scissors]
computer_choice = random.choice(weapons)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
user_weapon = weapons[user_choice]

print(f"You chose {user_weapon}")
print(f"Computer chose {computer_choice}")

if user_weapon == computer_choice:
    print("Its a draw! Let's go again.")
elif user_weapon == rock and computer_choice == paper:
        print("Paper beats rock, You Lose!")
elif user_weapon == paper and computer_choice == scissors:
    print("Scissors beats paper, You Lose!")
elif user_weapon == scissors and computer_choice == rock:
    print("Rock beats scissors, You Lose!")
elif user_weapon == scissors and computer_choice == paper:
    print("Scissors beat paper, You Win!")    
elif user_weapon == paper and computer_choice == rock:
    print("Paper beats rock, You Win!")   
    
else:
    print("Rock beats paper, You win!")

    
        
        
    

# print(computer_choice)
