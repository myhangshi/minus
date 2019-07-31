def calc_3_5(n): 
    sum = 0
    for i in range(2, n): 
        if i % 3 == 0: 
            sum += i
        elif i % 5 == 0: 
            sum += i
    return sum 

result = calc_3_5(1000) 
print(result) 

