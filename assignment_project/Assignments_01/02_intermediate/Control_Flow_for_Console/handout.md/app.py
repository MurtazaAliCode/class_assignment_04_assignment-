# import random

# score = 0

# rounds = int(input("How many rounds do you want to play? "))

# for _ in range(rounds):

#     player_number = random.randint(1, 100)
#     computer_number = random.randint(1, 100)

#     print(f"\nYour number is: {player_number}")

#     guess = input("Do you think your number is (H)igher or (L)ower than the computer's? ").strip().upper()

#     if (guess == "H" and player_number > computer_number) or (guess == "L" and player_number < computer_number):
#         print("Correct! You get a point!")
#         score += 1
#     else:
#         print("Wrong guess!")

#     print(f"The computer's number was: {computer_number}")

# print(f"\nGame over! Your final score is: {score}/{rounds}")

