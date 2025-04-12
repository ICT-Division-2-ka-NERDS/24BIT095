def count_vowels(string: str) -> int:
    
    if string == "":
        return 0
    elif string[0] in "aeiouAEIOU":
        return 1 + count_vowels(string[1:])
    else:
        return count_vowels(string[1:])

user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))
