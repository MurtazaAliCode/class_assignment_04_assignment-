def double_numbers(numbers):

    """Returns a new list with each element doubled."""
    return [num * 2 for num in numbers]

numbers = [1, 2, 3, 4]
numbers = double_numbers(numbers)

print(numbers)  

