#10.1
f1 = lambda x : x * x
print(type(f1))

def f2(x):
    return x*x
print(type(f2))

#10.2
#f = lambda x : x*x
#print(f(10,10))

#f = lambda x, y : x + y
#print(f(10))
  
  #오류 발생 이유: z를 선언해주지 않음
#f = lambda x, y : z = 100, x + y +z 
#print(f(10,20))

#10.3
persons = [('Gildong','Hong',27), ('SunSin','Lee',46),('YuSin','Gim',34)]
print(sorted(persons, key=lambda x : x[1])) 
print(sorted(persons, key=lambda x : x[2], reverse = True)) 

#10.6
n_list = [44,66,34,24,144,98,38,568,234,345]
new_list = [x for x in n_list if x%12==0]
print(new_list)

#10.9
new_list = [x for x in range(1,101) if x%6==0]
print(new_list)

#10.10
new_list = [x for x in range(1,101) if x%6==0 and x%7==0]
print(new_list)