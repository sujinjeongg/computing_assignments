#lab10-1-1
def sub(x,y):
    return x-y
print('200 - 100 =',sub(200,100))

#lab10-1-2
sub = lambda x,y: x - y
print('200 - 100 =',sub(200,100))

#lab10-2-1
def even_func(n):
    if n%2 == 0:
        return True
    else:
        return False
n_list = [1,2,3,4,5,6,7,8,9,10]
even_list = []
for even in filter(even_func, n_list):
    even_list.append(even)
print(even_list)

#lab10-2-2
def odd_func(n):
    if n%2 != 0:
        return True
    else:
        return False
n_list = [1,2,3,4,5,6,7,8,9,10]
odd_list = []
for odd in filter(odd_func, n_list):
    odd_list.append(odd)
print(odd_list)

#lab10-3-1
def upper(x):
    return x.upper()
a_list = ['a','b','c','d']
upper_a_list = list(map(lambda x: x.upper(), a_list))
print('upper_a_list =',upper_a_list)

#lab10-3-2
def twice(x):
    return x*2
def triple(x):
    return x*3
n_list = [10,20,30]
twice_list = list(map(lambda x:x*2, n_list))
triple_list = list(map(lambda x:x*3, n_list))
print('입력 값의 두 배 :',twice_list)
print('입력 값의 세 배 :',triple_list)

#lab10-4-1
from functools import reduce
a = []
for i in range(1,101):
    a.append(i)
n = reduce(lambda x,y: x+y, a)
print('1부터 100까지의 합 :',n)

#lab10-4-2
from functools import reduce
a = []
for i in range(1,11):
    a.append(i)
n = reduce(lambda x,y: x*y, a)
print('10! =',n)

#lab10-5-1
cubic = [x**3 for x in range(1,11)]
print('cubic =',cubic)

#lab10-5-2
a = ['welcome','to','the','python','world']
first_a = [a[i][0] for i in range(0,5)]
print('first_a =',first_a)

#lab10-6-1
cubic = [x**3 for x in range(1,11) if x<=500]
print(cubic)

#lab10-6-2
#모르는 문제

#lab10-7-1
class EvenCounter:
    def __init__(self, n = 0):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < 10:
            t = self.n
            self.n += 2
            return t
        raise StopIteration
my_even = EvenCounter()
for x in my_even:
    print(x,end = ' ')
print()

#lab10-7-2
class EvenCounter:
    def __init__(self, n = 0):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < 22:
            t = self.n
            self.n += 2
            return t
        raise StopIteration
my_even = EvenCounter()
for x in my_even:
    print(x,end = ' ')    

#lab10-8-1
txt = 'Welcome to Busan Metropolitan City'
print(txt.split())

#lab10-8-2
greet = 'Hello, My name is DongMin, Good to see you again'
print(greet.split(','))

#lab10-8-3
fruits = 'Apple|Banana|Melon|Orange'
print(fruits.split('|'));

