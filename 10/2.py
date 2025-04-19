def q2():
    
    students_data={}
    f=open('2.csv','r')
    lines=f.readlines()
    for line in lines[1:]:           #strt with one bcoz we dont want headings
        data=line.strip().split(',')
        rollNo=int(data[0])
        name=data[1]
        sub1=int(data[2])
        sub2=int(data[3])
        sub3=int(data[4])
        total=sub1+sub2+sub3
        students_data[rollNo]={"Name":name,"Sub1":sub1, "Sub2":sub2, "sub3":sub3, "Total":total}
    print(students_data)
    
q2()