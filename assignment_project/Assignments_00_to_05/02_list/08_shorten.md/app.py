MAX_LENGTH = 3  # Set the maximum length

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove and get the last item
        print(removed_item)  # Print the removed item

# Main function to get user input
def main():
    n = int(input("Enter the number of elements in the list: "))
    user_list = []

    for _ in range(n):
        element = input("Enter an element: ")
        user_list.append(element)

    shorten(user_list)  # Call the function
    print("Final list:", user_list)  # Print the remaining list

# Run the program
main()
