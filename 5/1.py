import random

odd_integers = random.sample(range(1, 100, 2), 5)
print("List of 5 odd integers:", odd_integers)

even_integers = random.sample(range(2, 100, 2), 4)
print("List of 4 even integers:", even_integers)

odd_integers[2] = even_integers
print("Updated list after replacing the third element of odd integers with even integers:", odd_integers)

flattened_list = []
for item in odd_integers:
    if type(item) == list:
        flattened_list.extend(item)
    else:
        flattened_list.append(item)
print("Flattened list:", flattened_list)

sorted_list = sorted(flattened_list)
print("Sorted list:", sorted_list)