def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print('The number of vowels in the string is:',vowel_count)