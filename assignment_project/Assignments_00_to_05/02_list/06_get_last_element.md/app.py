def get_last_element(lst):
    
    print(lst[-1])  

n = int(input("Enter the number of elements in the list: "))
user_list = []

for _ in range(n):
    element = input("Enter an element: ")
    user_list.append(element)

get_last_element(user_list)
