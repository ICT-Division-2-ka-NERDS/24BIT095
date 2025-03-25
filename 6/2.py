def student():

        lst=[(95,'Dhyey',18),(161,'Yesha',18),(143,'Jay',19),(144,'Arpit',17),(133,'Shaival',18),(147,'Anouskha',18)]
        roll=[i[0] for i in lst]
        name=[i[1] for i in lst]
        age=[i[2] for i in lst]
        print(roll,name,age)

student()