def sanitize_list(lst):
    
    if not lst:
        return []
    
    first = 0 if lst[0] < 0 else lst[0]
    return [first] + sanitize_list(lst[1:])

# Example usage
numbers = [5, -3, 7, -1, 0, -8, 10]
sanitized_numbers = sanitize_list(numbers)
print("Original list:", numbers)
print("Sanitized list:", sanitized_numbers)