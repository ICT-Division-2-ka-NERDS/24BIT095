def length():
    
    def filterFaculty(faculty: list):
        
        return list(filter(lambda x: len(x) > 8, faculty))
    
    faculty_names = ["afng ad", "FMSMN GWEIN", "GYUKVDCQA", "Gasdfasdfnsdno", "GWEIN"]
    filtered_names = filterFaculty(faculty_names)
    print("Filtered names (length > 8):", filtered_names)

length()