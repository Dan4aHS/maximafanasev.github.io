import math
from decimal import Decimal
from fractions import Fraction
import random
import copy
print('#1', 'True' if True else 'False')
print('#2', 'True' if False else 'False')
print('#3', 'text')
print('#4', 1, 2, 3, sep=' ')
print('#5', *[1,2,3], sep='\n')
print('#6', (2+4)*2)
print('#7', 2+4*2)
print('#8', 2+4.0)
print('#9', 0.1 + 0.1 + 0.1)
print('#10', 0.1 + 0.1 + 0.1 - 0.3)
print('#11', int(3.1415))
print('#12', float(3))
print('#13', 3**2)
print('#14', 144 ** .5)
print('#15', pow(144, .5))
print('#16', math.sqrt(144))
print('#17', 4/2+3)
print('#18', 1/3.0)
print('#19', 10/4)
print('#20', 10//4)
print('#21', 10//4.0)
print('#22', 5//-2)
print('#23', 25%6)
print('#24', math.floor(2.5))
print('#25', math.floor(-2.5))
print('#26', math.trunc(2.5))
print('#27', math.trunc(-2.5))
print('#28', math.pi)
print('#29', math.e)
print('#30', abs (-42.0))
print('#31', sum((1, 2, 3, 4)))
print('#32', min(3, 1, 2, 4))
print('#33', max(3, 1, 2, 4))
print('#34', 2<4 and 4<6)
print('#35', 2<4>6)
print('#36', 1<2<3.0<4)
print('#37', 1>2>3.0>4)
print('#38', 1==2<3 (1==2 and 2<3))
print('#39', 1.1+2.2 == 3.3)
print('#40', int(1.1+2.2) == int(3.3))
print('#41', 1j * 1J)
print('#42', 2 + 1j * 3)
print('#43', (2+1j)*3)
print('#44', 0o1)
print('#45', 0xFF)
print('#46', 0b10000)
print('#47', oct(64))
print('#48', hex(64))
print('#49', bin(64))
print('#50', eval('64'))
print('#51', 1 << 2)
print('#52', 1 | 2)
print('#53', 1 & 1)
print('#54', '%e'%0.33333)
print('#55', '%4.2f'%0.333333)
print('#56', '{0:4.2f}'.format(0.333))
print('#57', Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print('#58', Fraction (4, 6))
print('#59', random.choice(['a', 'b', 'c']))
print('#60', random.shuffle(['a', 'b', 'c']))
print('#61', 'banana'.count('a'))
print('#62', 'Hello, welcome'.find('welcome'))
print('#63', 'Mi casa, su casa.'.index('casa'))
print('#64', sorted('cba'))
print('#65', 'Ёёж'.replace('Ё', 'Е').replace('ё', 'е'))
print('#66', 'h'.capitalize())
print('#67', 'Hello My'.swapcase())
print('#68', 'Welcome to'.title())
print('#69', 'Hello my friends'.upper())
print('#70', 'Hello my FRIENDS'.lower())
print('#71', 'Hello, And'.casefold())
print('#72', 'banana'.center(20, 'O'))
print('#73', 'H\te\tl\tl\to'.expandtabs())
print('#74', 'For only {price:.2f} dollars!'.format(price = 49))
print('#75', '#'.join(['John', 'Peter', 'Vicky']))
print('#76', 'welcome to the jungle'.split())
print('#77', ' spacious '.strip())
print('#78', 'spacious '.rstrip())
print('#79', 'Hello, welcome to my world.'.startswith('Hello'))
print('#80', True)
print('#81', 'world.'.endswith('.'))
print('#82', True)
print('#83', '50'.zfill(10))
print('#84', [1, 2].append(3))
print('#85', [1, 2].extend([3, 4]))
print('#86', [1, 2].insert(1,'a'))
print('#87', [1, 2].index(2))
print('#88', [1, 2].count(2))
print('#89', sorted(['b','c','a']))
print('#90', ['b','c','a'].reverse())
print('#91', copy.copy(['b','c','a']))
print('#92', [1,2].clear())
print('#93', ['a','b'].pop(1))
print('#94', [1,2].remove(1))


