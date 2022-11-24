#9.1
print((123).__add__(334))
print((123).__sub__(334))
print((123).__mul__(334))
print((123).__truediv__(3))

#9.2
fruit_list = ['apple','banana','mango','pear','grape']
fruit_list.pop()
fruit_list.sort()
fruit_list.append('peach')
#fruit_list.upper() 사용 불가능한 메소드
fruit_list.insert(3,'peach')
fruit_list.remove('apple')

#9.5
a = 1
b = 1
c = 2
d = 3
e = 3
print('a와 b는 같은 객체인가?',a is b)
print('b와 c는 같은 객체인가?',b is c)
print('c와 d는 같은 객체인가?',c is d)
print('d와 e는 같은 객체인가?',d is e)

#9.6
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print('my_dog의 이름은 {}이고, 나이는 {}살입니다.'.format(self.name, self.age))
my_dog = Dog('Mango',3)
my_dog.introduce()

#9.7
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'my_dog의 이름은 '+self.name+'이고, 나이는 '+str(self.age)+'살입니다.'
my_dog = Dog('Mango',3)
print(my_dog)

