#4-1-1
#함수 호출문을 삭제하면 아무것도 출력되지 않는다.

#4-1-2
def print_star():
    print('********************')
print_star()
print_star()
print_star()
print_star()
print_star()
print_star()

print() #문제번호 구별

#4-2
def print_star5():
    print('********************')
    print('********************')
    print('********************')
    print('********************')
    print('********************')
print_star5()
print_star5()

print() #문제번호 구별

#4-3-1
def print_hash():
    print('#####################')
print_hash()

print() #문제번호 구별

#4-3-2
def print_star():
    print('*********************')
def print_plus():
    print('+++++++++++++++++++++')
print_hash()
print_star()
print_plus()
print_plus()
print_star()
print_hash()

print() #문제번호 구별

#4-4-1
def print_star(n):
    for _ in range(n):
        print('*****************')
print_star(10)

print() #문제번호 구별

#4-4-2
def print_hash(n):
    for _ in range(n):
        print('#################')
print_hash(10)

print() #문제번호 구별

#4-4-3
def print_hash(n):
    for _ in range(n):
        print('#################')
print_hash(6)

print() #문제번호 구별

#4-4-4
def print_hash(n):
    for i in range(n):
        print(i,'#################')
print_hash(6)

print() #문제번호 구별

#4-5-1
def print_sub(a,b):
    result = a- b
    print(a,'과',b,'의 차는',result,'입니다.')
print_sub(10,20)

print() #문제번호 구별

#4-5-2
def print_mult(a,b):
    result = a*b
    print(a,'과',b,'의 곱은',result,'입니다.')
print_mult(10,20)

print() #문제번호 구별

#4-6-1
def print_root(a,b,c):
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    print('해는',r1,'또는',r2)
print_root(1,4,-21)
print_root(1,-6,8)

print() #문제번호 구별

#4-6-2
def print_area(width, height):
    result = 0.5 * width * height
    print('밑변',width,', 높이',height,'인 삼각형의 면적은 :',result)
print_area(10,20)

print() #문제번호 구별

#4-7
radius = 10
def circle_area_circum(radius):
    a= radius **2 * 3.14
    c = radius*2*3.14
    return a, c
area, circum = circle_area_circum(radius)
circum = round(circum, 1) #소수점 지정
print('반지름',radius,'인 원의 면적은',area,'원의 둘레는',circum)

print() #문제번호 구별

#4-8
def multiplies(n,m):
    tup = ()
    for i in range(1,m+1):
        tup = tup + (n*i,)
    return tup
r1,r2,r3,r4 = multiplies(3,4)
print(r1,r2,r3,r4)
r1,r2,r3,r4,r5 = multiplies(2,5)
print(r1,r2,r3,r4,r5)

print() #문제번호 구별

#4-9
def print_name(honorifics, first_name, last_name):
    print(honorifics, first_name,last_name)
print_name(first_name = 'Gildong', last_name = 'Hong',honorifics = 'Dr.')
print_name('Gildong','Hong','Dr.')

print() #문제번호 구별

#4-10-1
def sum_nums(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(len(numbers),'개의 인자',numbers)
    print('합계 :',result,'평균 :',result/len(numbers))
sum_nums(10,20,30)
sum_nums(10,20,30,40,50)

print() #문제번호 구별

#4-10-2
def min_nums(*numbers):
    min = numbers[0]
    for n in numbers:
        if n < min:
            min = n
    print('최솟값은',min)
min_nums(20,40,50,10)

print() #문제번호 구별

#4-11-1
name = input('당신의 이름을 입력해주세요 :')
age = int(input('나이를 입력해주세요 :'))
job = input('직업을 입력해주세요 :')
home = input('사는 곳을 입력해주세요 :')
print('당신의 이름은 {},나이는 {}살, 직업은 {},사는 곳은 {}입니다.'.format(name,age,job,home))
print('당신의 이름은',name,',나이는',age,'살, 직업은',job,',사는 곳은',home,'입니다.')

print() #문제번호 구별

#4-12-1
print('_'.join('ABCD'))

#4-12-2
s = 'My favorite thing is monsters.'
t = s.replace('monsters','cartoons')
print(t)

