# Mars gravity factor
MARS_GRAVITY = 0.378

earth_weight = float(input("Enter your weight on Earth (kg): "))

mars_weight = earth_weight * MARS_GRAVITY

print(f"Your weight on Mars would be: {round(mars_weight, 2)} kg")
