#3-1

game_score = int(input("game_score ="))

if game_score > 1000:

    print("당신은 고수입니다.")

 

#3-1-2

num_a = 100

num_b = 200

print("num_a =", num_a,  "num_b =", num_b )

if num_a == num_b:
    print("두 값이 일치합니다.")

 

num_a = 300

num_b = 300

if num_a == num_b:

    print("num_a =", num_a, "num_b =", num_b )

    print("두 값이 일치합니다.")

 

#3-2-1

n = int(input("정수를 입력하세요: "))

print("n = ", n)

if n % 2 == 0 :

    print(n,"은 짝수입니다.")

 

#3-2-2

x = int(input("정수를 입력하세요 : "))

print("x =", x)

if x > 0:

    print(x,"은 자연수입니다.")

 

#3-3-1

game_score = int(input('게임점수를 입력하시오 : '))

print("game_score =", game_score)

if game_score > 1000:

    print("고수입니다.")

else:

    print("입문자입니다.")

 

#3-3-2

a = int(input('한 정수를 입력하시오 : '))

b = int(input("다른 정수를 입력하시오 : "))

if a == b:

    print("두 값이 일치합니다.")

else:

    print("두 값이 일치하지 않습니다.")

 

#3-3-3-1

adult = int(input('당신은 성인인가요(성인이면 1, 미성년이면 0): '))

if adult == 0:

    print("당신은 미성년자입니다.")

 

#3-3-3-2

adult = int(input('당신은 성인인가요(성인이면 1, 미성년이면 0): '))

if adult == 0:

    print("당신은 미성년자입니다.")

elif adult == 1:

    marry = int(input("결혼을 하셨나요(기혼이면 1, 미혼이면 0): "))

    if marry == 1:

        print("당신은 결혼한 성인입니다.")

    elif marry == 0:

        print("당신은 결혼하지 않은 성인입니다.")

 

#3-4-1

num = 2
print("num =", num)
print(1<num and num<10)

 

#3-4-2

age = 9
print("age =", age)
if 10 < age and age < 19:

    print("청소년입니다.")

    

age = 12
print("age =", age)
if 10 < age and age < 19:

    print("청소년입니다.")

 

#3-5-1

speed = int(input("자동차의 속도를 입력하세요(단위 : km/h): "))

if speed >= 100:

    print("고속")

elif 60 <= speed < 1000:

    print("중속")

else:

    print("저속")

 

#3-5-2

micro = int(input("미세먼지 농도를 입력하세요(단위 : microgram/m^3 0; "))

if 0 <= micro<=15:

    print("좋음")

elif 16<= micro <=35:

    print("보통")

elif 36<=micro<=75:

    print("나쁨")

elif micro >= 76:

    print("매우 나쁨")

 

#3-6-1

for _ in range(5):

    print("Hello, Python!")

 

#3-6-2

for i in range(0,5):

    print(i)

 

#3-7-1

print(list(range(1, 101)))

 

#3-7-2

print(list(range(2,101,2)))

 

#3-7-3

print(list(range(1,101,2)))

 

#3-7-4

print(list(range(-99,0)))

 

#3-8-1
s = 0
for i in range(1,101):
    s = s + i
print(s)

#3-8-2
s = 0
for i in range(0,101,2):
    s = s + i
print(s)

#3-8-3
s= 0
for i in range(1,101,2):
    s = s + i
print(s)

#3-9
n= 7
for i in range(n):
    for j in range(n-(i+1)): #공백을 출력함
        print(' ', end = '')
    print('#')
