import random

secret_number = random.randint(0, 10)

print("I am thinking of a number between 0 and 10...")

while True:
    try:
        guess = int(input("Enter a guess: "))
        
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit the loop when the correct guess is made
    except ValueError:
        print("Please enter a valid number.")
