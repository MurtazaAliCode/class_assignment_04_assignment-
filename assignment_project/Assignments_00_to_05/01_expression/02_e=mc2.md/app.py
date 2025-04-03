# Define the speed of light as a constant (in meters per second)

C = 299792458  

while True:
    try:
        mass = float(input("Enter kilos of mass (or type '0' to exit): "))
        
        if mass == 0:
            print("Exiting program...")
            break

        energy = mass * C**2

        print("\ne = m * C^2...\n")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!\n")

    except ValueError:
        print("Invalid input! Please enter a numeric value.\n")
