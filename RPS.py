import random
options = ["Rock, Paper, Sciscors"]
user_choice = input("Choose Rock, Paper or Scissors?: ")
computer_choice = random.choice(options)
print("You choose, user_choice")
print("Computer choose, computer_choice")
if user_choice == computer_choice:
    print("its a tie!")
elif user_choice == "Rock" and computer_choice == "Scisscors":
    print("Rock smashes paper!, You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers rock!, You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cut paper!, You win!")
else:
    print("You lose!")

    