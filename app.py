from random import randint

name = input("What is your name? ")
age = int(input("How old are you? "))
year = 2026 + (18 - age)
print("Hello " + name + "! You will turn 18 in the year " + str(year))
print("I am learning DevOps!")
print("This is an update")

user_choice = input("Please choose Rock, Paper, Scissor")
randnumber = randint(1,3)

if random_num == 1:
    comp_choice = "stone"
elif random_num == 2:
    comp_choice = "paper"
else:
    comp_choice = "scissors"
    
print(f"Computer chose: {comp_choice.capitalize()}")

if user_choice == comp_choice:
    print("🤝 It's a tie!")
elif user_choice == "stone" and comp_choice == "scissors":
    print("🎉 You win! Stone crushes Scissors.")
elif user_choice == "paper" and comp_choice == "stone":
    print("🎉 You win! Paper covers Stone.")
elif user_choice == "scissors" and comp_choice == "paper":
    print("🎉 You win! Scissors cut Paper.")
else:
    print("💻 Computer wins!")
