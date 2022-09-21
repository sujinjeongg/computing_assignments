#Q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#Q2
s = 0
i = 1
while i<=1000:
    if i  %3 == 0:
        s = s + i
    i += 1
print('1부터 1000까지의 자연수 중 3의 배수의 합: ',s)

#Q3
line = 0
star = 0

while line < 5:
    line = line  + 1
    star = 0
    while star < line:
        star = star + 1
        print("*", end = '')
    print()

#Q4
for i in range(1,101):
    print(i)

#Q5
score = [70,60,55,75,95,90,80,80,85,100]
s = 0
for i in range(len(score)):
    s = s + score[i]
average = s / 10
print('A 학급의 평균 점수 : ', average)
    
#Q6
numbers = [1,2,3,4,5]
result = [x*2 for x in numbers if x % 2 != 0]
print(result)
