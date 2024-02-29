import os
print('-----------------')
#создать ссылку из строк
print('#1', os.path.join('usr', 'bin', 'spam')) 
#текущий каталог
print('#2', os.getcwd()) 
#изменить путь до каталога
print('#3', os.chdir('C:\\Windows')) 
# каталог изменился
print('#4', os.getcwd()) 
#создать папку 1 раз
#print('#5', os.makedirs('C:\\Users\\Swizi\\Desktop\\www'))
print('-----------------')
print('#1', os.path.abspath('.'))
print('#2', )
print('#3', )
print('#4', )
print('#5', )

