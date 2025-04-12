def string_length(s):
   
    if s == "":
        return 0
    return 1 + string_length(s[1:])

text = "Ora Ora Ora Ora"
length = string_length(text)
print("String:", text)
print("Length:", length)