#1
celsius = 0
for celsius in range(0,51,5):
    fahrenheit = (9/5) * celsius + 32
    print('섭씨온도 : ',celsius, '화씨온도 : ',fahrenheit)

#2
a = 2*2//2
b = 3//2*3
print(a,b)
    
#3
s = 0
for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        s = s + i
print('1000미만의 자연수에서 3의 배수와 5의 배수의 총합 : ', s)
