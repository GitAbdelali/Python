def leap(year): 
    if year%400 == 0: 
        return True 
    elif year%4 ==0 and year%100!=0: 
        return True 
    else: 
        return False 

print(leap(2008))
print(leap(1900))
print(leap(2000))