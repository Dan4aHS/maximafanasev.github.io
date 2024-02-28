def isPhoneNumber(text):
    
    if len(text) != 12: # содержит ли строка 12 символов?
        return False
    
    for i in range(0, 3):
        if not text[i].isdecimal(): # 3 символа цифры?
            return False
        
    if text[3] != '-': #дефис?
        return False
    
    for i in range(4, 7):
        if not text[i].isdecimal(): # 3 символа цифры?
            return False
        
    if text[7] != '-': #дефис?
        return False
    
    for i in range(8, 12): # 3 символа цифры?
        if not text[i].isdecimal():
            return False
        
    return True 


print(isPhoneNumber('415-555-4242'))
print(isPhoneNumber('415xx555-4242'))
print(isPhoneNumber('415-5A5-4242'))
print(isPhoneNumber('Не телефонный номер, а фигня'))
