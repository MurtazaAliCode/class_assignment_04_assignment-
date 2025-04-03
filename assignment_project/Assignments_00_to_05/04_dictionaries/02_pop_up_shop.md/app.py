def main():
    # Dictionary of fruits with their prices
    fruit_prices = {
        "apple": 5.0,
        "durian": 15.0,
        "jackfruit": 12.5,
        "kiwi": 7.0,
        "rambutan": 3.5,
        "mango": 8.0
    }
    
    total_cost = 0
    
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
