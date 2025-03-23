def upper_case():

    strings = ["Hitler", "Himmler", "Goebbels", "Goring","Mengele"]
    for i in range(len(strings)):
        strings[i] = strings[i].upper()
    print(strings)

upper_case()