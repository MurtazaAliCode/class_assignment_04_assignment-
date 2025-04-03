number_counts = {}

while True:
    num = input("Enter a number (or press Enter to stop): ")

    if num == "":
        break

    num = int(num)  

    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1

for number, count in number_counts.items():
    print(f"{number} appears {count} times.")
