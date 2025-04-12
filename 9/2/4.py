def reverse_list(lst):
    
    if len(lst) <= 1:
        return lst
    
    return reverse_list(lst[1:]) + [lst[0]]

numbers = [1,4,2,5,2,5,16,7,8,12]
reversed_numbers = reverse_list(numbers)
print("Original list:", numbers)
print("Reversed list:", reversed_numbers)