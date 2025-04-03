import math

def main():
    # Get the lengths of the two perpendicular sides from the user
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    
    # Calculate the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab ** 2 + ac ** 2)
    
    # Output the result
    print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

# Run the program
if __name__ == "__main__":
    main()
