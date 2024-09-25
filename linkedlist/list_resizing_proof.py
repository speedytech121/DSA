import sys

# Function to show the size of the list and its capacity
def show_list_info(lst):
    print(f"List length: {len(lst)}, List size in bytes: {sys.getsizeof(lst)} bytes")

# Start with an empty list
my_list = []

# Show initial information
show_list_info(my_list)

# Append elements and monitor the size
for i in range(10):
    my_list.append(i)
    show_list_info(my_list)

# Continue appending more elements to observe resizing
for i in range(10, 20):
    my_list.append(i)
    show_list_info(my_list)
