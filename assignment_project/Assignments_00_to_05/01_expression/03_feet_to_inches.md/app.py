while True:
    try:
        
        feet = float(input("Enter length in feet (or type '0' to exit): "))

        if feet == 0:
            print("Exiting program...")
            break

        inches = feet * 12

        unit = "foot" if feet == 1 else "feet"  # Singular vs plural
        print(f"{feet} {unit} is equal to {inches} inches.\n")

    except ValueError:
        print("Invalid input! Please enter a numeric value.\n")
