def missing_numbers(num_list):
    c = sorted(num_list)
    for i in range(1,len(c)+1):
        if i not in c:
            return i
       


print(missing_numbers([1, 2, 4,5, 6, 7,8,9,10]))

