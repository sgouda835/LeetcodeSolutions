def plusOne(digits):
    idx = len(digits) - 1
        
    while idx >= 0:
        if digits[idx] == 9:
            digits[idx] = 0
        else:
            digits[idx] += 1
            return digits
        idx -= 1   
    return [1] +digits

digits= [1,0,0,9]
print(plusOne(digits))
