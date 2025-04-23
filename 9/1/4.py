def calculate_sum():
    def sum_avg(*arg): 
        total = sum(arg) 
        avg = total / len(arg)  
        return total, avg

    total, avg = sum_avg(100, 100, 100, 100, 100)
    print("Total:", total)
    print("Average:", avg)

calculate_sum()
