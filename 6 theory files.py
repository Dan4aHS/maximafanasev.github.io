import os
print('-----------------')
# создать ссылку из строк
print('#1', os.path.join('usr', 'bin', 'spam')) 
# текущий каталог
print('#2', os.getcwd()) 
# изменить путь до каталога
print('#3', os.chdir('C:\\Windows')) 
# каталог изменился
print('#4', os.getcwd()) 
# создать папку 1 раз
# print('#5', os.makedirs('C:\\Users\\Swizi\\Desktop\\www'))
print('-----------------')
# aбсолютный путь
print('#1', os.path.abspath('.'))
# перейти в папку Scripts
print('#3', os.path.abspath('.\\Scripts'))
# проверка на абсолютный путь
print('#3', os.path.isabs('.'))
# возврат строки относительного пути
print('#4', os.path.relpath('C:\\Windows'))
print('#5', )

