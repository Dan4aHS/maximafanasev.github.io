import copy
print('-----------------')
print('#1', [1, 2].append(3))
print('#2', [1, 2].extend([3, 4]))
print('#3', [1, 2].insert(1,'a'))
print('#4', [1, 2].index(2))
print('#5', [1, 2].count(2))
print('-----------------')
print('#1', sorted(['b','c','a']))
print('#2', ['b','c','a'].reverse())
print('#3', copy.copy(['b','c','a']))
print('#4', [1,2].clear())
print('#5', ['a','b'].pop(1))
print('-----------------')
print('#1', len([1, 2, 3]))
print('#2', [1, 2, 3] + [4, 5, 6])
print('#3', ['a'] * 4)
print('#4', str([1, 2]) + '34')
print('#5', [1, 2] + list('34'))
print('-----------------')
print('#1', 3 in [1, 2, 3])
print('#2', [с * 4 for с in 'SPAM'])
print('#3', list(map(abs, [-1, -2, 0, 1, 2])))
print('#4', ['a', 'b', 'c'][0])
print('#5', ['a', 'b', 'c'][-2])
print('-----------------')
print('#1', ['a', 'b', 'c'][:1])
print('#2', ['a', 'b', 'c'][1:])
print('#3', [[1, 2, 3], [4, 5, 6], [7, 8, 9]][1][1])
a = ['a', 'b', 'c']
a[1]='D'
print('#4', a)
a[1:1] = [6,7]
print('#5', a)
print('-----------------')
a = [2, 3, 4, 1]
a[len(a):] = [5, 6, 7]
print('#1', a)
a = [ 'abc', 'ABD', 'aBe']
a.sort()
print('#2', a)
a.sort (key=str.lower)
print('#3', a)
a.sort(key=str.lower, reverse=True)
print('#4', a)
