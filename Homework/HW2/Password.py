def password_check(newP, oldP):
    if(len(newP)>=6):
        if(newP != oldP):
            return True
    return False

print(password_check('E10-s2ff', 'E10.s2ff'))
print(password_check('E10sf', 'E10.s2ff'))
print(password_check('E10-s2ff', 'E10-s2ff'))