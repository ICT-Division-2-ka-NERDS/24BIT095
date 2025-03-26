def employment():
    employees = {1: [13, 25000],2: [16, 70000],3: [13, 35000],4: [12, 69000],5: [12, 8000], 6: [11, 44000],7: [10, 500],8: [731, 11000],9: [10, 60000],}
    dept_salary_stats = {}
    
    for emp_no, emp_info in employees.items():
        dept_no = emp_info[0] 
        salary = emp_info[1]

        if dept_no not in dept_salary_stats:
            dept_salary_stats[dept_no] = [salary, salary]  
        else:
            dept_salary_stats[dept_no][0] = min(dept_salary_stats[dept_no][0], salary)
            dept_salary_stats[dept_no][1] = max(dept_salary_stats[dept_no][1], salary)

    for dept_no, stats in dept_salary_stats.items():
        print(f"Department {dept_no}: Min Salary = {stats[0]}, Max Salary = {stats[1]}")

employment()