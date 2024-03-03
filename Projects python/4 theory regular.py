import re
a = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(a.search('Мой номер: 415-555-4242.').group())

b = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print('#1', b.search('Мой номер: 415-555-4242.').group())
print('#2', b.search('Мой номер: 415-555-4242.').group(0))
print('#3', b.search('Мой номер: 415-555-4242.').group(1))
print('#4', b.search('Мой номер: 415-555-4242.').group(2))
print('#5', b.search('Мой номер: 415-555-4242.').group(1,2))
print('#6', b.search('Мой номер: 415-555-4242.').groups())




print('-'*20)
print('-'*20)
print('-'*20)




d = re.compile(r'Batman|Tina Fey')
print('#1', d.search('Batman and Tina Fey.').group())
print('#2', d.search('Tina Fey and Batman.').group())

e = re.compile(r'Bat(man|mobile|copter|bat)')
print('#3', e.search('Batmobile потерял колесо'))
print('#4', e.search('Batmobile потерял колесо').group())
print('#5', e.search('Batmobile потерял колесо').group(1))





print('-'*20)
print('-'*20)
print('-'*20)




j = re.compile(r'Bat(wo)?man')
print('#1', j.search('The Adventures of Batman'))
print('#2', j.search('The Adventures of Batman').group())
print('#3', j.search('The Adventures of Batwoman').group())

k = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
print('#4', k.search('Мой номер: 415-555-4242').group())
print('#5', k.search('Мой номер: 555-4242').group())





print('-'*20)
print('-'*20)
print('-'*20)




l = re.compile(r'Bat(wo)*man')
# * это 0 или более
print('#1', l.search('The Adventures of Batman').group())
print('#2', l.search('The Adventures of Batwowowoman').group())

q = re.compile(r'Bat(wo)+man')
# + это один и более
print('#3', q.search('The Adventures of Batwoman').group())

w = re.compile(r'(Ha){3}')
print('#4', w.search('HaHaHa').group())




print('-'*20)
print('-'*20)
print('-'*20)



w = re.compile(r'(Ha){3,5}')
# жадный вид поиска берет по максимуму
print('#1', w.search('HaHaHa').group())
print('#2', w.search('HaHaHaHa').group())
print('#3', w.search('HaHaHaHaHa').group())

qq = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print('#4', qq.findall('Сотовый 444-222-5555, рабочий 333-111-3333'))

qq = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print('#5', qq.findall('Сотовый 444-222-5555, рабочий 333-111-3333'))




print('-'*20)
print('-'*20)
print('-'*20)


#d Любая от 0 до 9
#D любой символ не цифра от 0 до 9
#w любая буква, цифра или _
#W любой символ не являющийся буквой цифрой или _
#s символ пробела табуляции или новой строки
#S любой не пробел табуляция или новоя строка

ww = re.compile(r'^Hello')
# ^ начало строки
print('#1', ww.search('Hello motherf...').group())
print('#2', ww.search('motherf... Hello') == None)

ee = re.compile(r'Hello$')
# $ заканчивается этим
print('#3', ee.search('Hello motherf...') == None)
print('#4', ee.search('motherf... HHHHello').group())




print('-'*20)
print('-'*20)
print('-'*20)



rr = re.compile(r'.at')
# at групповой символ
print('#1', rr.search('The cat in the hat').group())
print('#2', rr.findall('The cat in the hat'))

tt = re.compile(r'First Name: (.*) Last Name: (.*)')
# at групповой символ
print('#3', tt.search('First Name: Max Last Name: Afanasev').groups())

tt = re.compile(r'<.*?>')
# at групповой символ
print('#4', tt.search('<aaaa> bbb>').group())

tt = re.compile(r'<.*>')
# at групповой символ
print('#5', tt.search('<aaaa> bbb>').group())











      



