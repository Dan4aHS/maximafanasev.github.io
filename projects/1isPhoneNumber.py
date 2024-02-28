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

import re
a = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(a.search('Мой номер: 415-555-4242.').group())

b = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print('#1', b.search('Мой номер: 415-555-4242.').group())
print('#2', b.search('Мой номер: 415-555-4242.').group(0))
print('#3', b.search('Мой номер: 415-555-4242.').group(1))
print('#4', b.search('Мой номер: 415-555-4242.').group(2))
print('#5', b.search('Мой номер: 415-555-4242.').group(1,2))

print('#1', b.search('Мой номер: 415-555-4242.').groups())

# TODO: выдает ошибку втф?
#c = re.compile(r'(\(\d\d\d)) (\d\d\d-\d\d\d\d)')
#print('#1', c.search('Мой номер: (415) 555-4242.').group(1))

d = re.compile(r'Batman|Tina Fey')
print(d.search('Batman and Tina Fey.').group())
print(d.search('Tina Fey and Batman.').group())

e = re.compile(r'Bat(man|mobile|copter|bat)')
print(e.search('Batmobile потерял колесо'))
print(e.search('Batmobile потерял колесо').group())
print(e.search('Batmobile потерял колесо').group(1))

j = re.compile(r'Bat(wo)?man')
print(j.search('The Adventures of Batman'))
print(j.search('The Adventures of Batman').group())
print(j.search('The Adventures of Batwoman').group())

k = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print(k.search('Мой номер: 415-555-4242').group())
print(k.search('Мой номер: 555-4242').group())

l = re.compile(r'Bat(wo)*man')
# * это 0 или более
print(l.search('The Adventures of Batman').group())
print(l.search('The Adventures of Batwowowoman').group())

q = re.compile(r'Bat(wo)+man')
# + это один и более
#print(q.search('The Adventures of Batman').group())
print(q.search('The Adventures of Batwoman').group())

w = re.compile(r'(Ha){3}')
# ошибка тк от 3х НаНаНа
# print(w.search('Ha').group())
# ошибка
# print(w.search('HaHa').group())
print(w.search('HaHaHa').group())

w = re.compile(r'(Ha){3,5}')
# жадный вид поиска берет по максимуму
print(w.search('HaHaHa').group())
print(w.search('HaHaHaHa').group())
print(w.search('HaHaHaHaHa').group())

qq = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(qq.findall('Сотовый 444-222-5555, рабочий 333-111-3333'))

qq = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(qq.findall('Сотовый 444-222-5555, рабочий 333-111-3333'))

#d Любая от 0 до 9
#D любой символ не цифра от 0 до 9
#w любая буква, цифра или _
#W любой символ не являющийся буквой цифрой или _
#s символ пробела табуляции или новой строки
#S любой не пробел табуляция или новоя строка










      



