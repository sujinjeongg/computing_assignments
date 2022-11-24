#lab9-1-1
print((200).__sub__(100))
print((200).__mul__(100))
print((200).__truediv__(100))

#9-1-2
print([10,20,30,40].pop())

#9-1-3
#리스트 객체가 호출할 수 없는 메소드:keys(),get()

#9-1-4
print(dir(int))

#9-1-5
print(dir(list))

#9-2-1
#객체 지향 프로그래밍 : 컴퓨터가 수행하는 작업을 객체들 사이의 상호작용으로 표현해보는 것
#절차적 프로그래밍 : 프로그램 작성을 효과적으로 하기 위해 함수나 모듈을 만들어두고 이것들을 문제해결 순서에 맞게 호출하여 수행되도록 하는 방식
#그래픽 사용자 인터페이스 : 사용자가 편리하게 사용할 수 있도록 입출력 등의 기능을 알기 쉬운 아이콘 따위의 그래픽으로 나타낸 것

#9-2-2
#절차지향은 데이터를 중심으로 함수를 구현하고, 이에 반해 객체지향은 기능을 중심으로 메소드를 구현하게 됩니다. 절차지향 언어를 사용한다면, 말 그래도 실행순서, 절차가 더 중점이 되고, 객체지향 언어를 사용한다면, 필요한 객체들의 종류와 속성 등이 더 중점이 됩니다.

#9-3
#클래스 : 객체들이 프로그램에서 동작할 수 있도록 하는 설계도
#객체 : 프로그램 상에서 사용되는 속성과 동작을 모아놓은 집합체 / 어떤 행위의 대상이 될 수 있는 모든 사물
#인스턴스 : 클래스로부터 만들어지는 개별적인 객체 / 클래스라는 추상적 틀에 근거해 만들어진 사물
#클래스의 속성 : 클래스 내부의 메소드 단계와 동일한 영역에 위치한 변수
#클래스의 동작 : 메소드라고도 한다.

#9-4
class Dog:
    def bark(self):
        print("멍멍~~")
my_dog = Dog()
my_dog.bark()

#9-5
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print('내 이름은 {}, 멍멍~~'.format(self.name))
my_dog = Dog('Jindo')
my_dog.bark()

#9-6
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'my_dog의 정보 : Dog(name = '+self.name+')'
my_dog = Dog('Jindo')
print(my_dog)

#9-7
#결과: n is m 이유: 정수는 불변 객체이기 때문이다.

#9-8-1
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
v1 = Vector2D(30,40)
v2 = Vector2D(10,20)

v3 = v1 * v2
print('v1 * v2 =',v3)
v4 = v1 / v2
print('v1 / v2 =',v4)

#9-8-2
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __neg__(self):
        return Vector2D(-(self.x), -(self.y))
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
v1 = Vector2D(10,20)

v3 = -(v1)
print('-v1 =',v3)

#9-9 #모르는 문제
# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __gt__(self, other):
#         return Vector2D(0.5**((self.x)**2 + (other.x)**2), 0.5**((self.y)**2 + (other.y)**2))
#     def __str__(self):
#         return '({}, {})'.format(self.x, self.y)
# v1 = Vector2D(30,40)
# v2 = Vector2D(10,20)

# v3 = v1 > v2
# print('v1 * v2 =',v3)

#9-10-1
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
r1 = Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['width'])

#9-10-2
class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
r1 = Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])

#9-11
a = 100
b = a 
print(id(a) == id(100))
print(id(b) == id(100))
print(id(a) == id(b))
a = 200
print(id(a) == id(200))
print(id(b) == id(200))
print(id(a) == id(b))

