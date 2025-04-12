def lower_case():
    def count_lower_upper(string:str):
        upper_Case=0
        lower_Case=0
        for i in string:
            if (i.isupper()):
                upper_Case+=1
            elif(i.islower()):
                lower_Case+=1
            else:
                pass
        return {"UpperCase":upper_Case,"LowerCase":lower_Case}
    s1="Eat tHe RiCh"
    print(count_lower_upper(s1))
lower_case()