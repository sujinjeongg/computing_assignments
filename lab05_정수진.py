#5-1
even_list = [2,4,6,8,10]
print('even_list =',even_list)

#5-1-2
even_list = list(range(2,12,2))
print('even_list =',even_list)

#5-1-3
nations = ['Korea','China','India','Nepal']
print('nations =',nations)

#5-1-4
friends = ['승철','정한','지수','도겸','민규']
print('friends =',friends)

#5-1-5
print('string =', list('XYZ'))

#5-2-1
prime_list = list() 
for i in range(2,11):
    is_prime = True
    for n in range(2,i):
        if i % n == 0:
            is_prime = False
    if is_prime:
        prime_list.append(i)
print('prime_list의 첫 원소 :', prime_list[0])
            
#5-2-2
prime_list = []
for i in range(2,11):
    is_prime = True
    for n in range(2,i):
        if i % n == 0:
            is_prime = False
    if is_prime:
        prime_list.append(i)
print('prime_list의 마지막 원소 :', prime_list[len(prime_list) - 1])

#5-2-3
prime_list = []
for i in range(2,11):
    is_prime = True
    for n in range(2,i):
        if i % n == 0:
            is_prime = False
    if is_prime:
        prime_list.append(i)
print('prime_list의 마지막 원소 :', prime_list[- 1])
        
#5-2-4
nations = ['Korea','China','Russia','Malaysia']
print('nations의 첫 원소 :', nations[0])

#5-2-5
nations = ['Korea','China','Russia','Malaysia']
print('nations의 마지막 원소 :', nations[-1])

#5-2-6
nations = ['Korea','China','Russia','Malaysia']
print('nations의 마지막 원소 :', nations[len(nations) - 1])

#5-3-1
prime_list = []
for i in range(2,11):
    is_prime = True
    for n in range(2,i):
        if i % n == 0:
            is_prime = False
    if is_prime:
        prime_list.append(i)
print('소수 목록 :',prime_list)
prime_list.append(11)
print('추가 후 소수 목록 :',prime_list)
        
#5-3-2
print('삭제 전 소수 목록 :',prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록 :',prime_list)

#5-3-3
nations = ['Korea','China','Russia','Malaysia']
print('국가 목록 :',nations)
nations.append('Nepal')
print('추가 후 국가 목록 :',nations)

#5-3-4
if 'Japan' in nations:
    print('Japan 는(은) 국가 목록에 있습니다.')
else:
    print('Japan 는(은) 국가 목록에 없습니다.')
if 'Russia' in nations:
    print('Russia 는(은) 국가 목록에 있습니다.')
else:
    print('Russia 는(은) 국가 목록에 없습니다.')

#5-4-1
prime_list = list()
for i in range(2,11):
    is_prime = True
    for n in range(2,i):
        if i % n == 0:
            is_prime = False
    if is_prime:
        prime_list.append(i)
print('1에서 10까지의 소수 :',prime_list)
print('최솟값 :',min(prime_list))
print('최댓값 :',max(prime_list))
print('합계 :',sum(prime_list))
print('평균 :',sum(prime_list) / len(prime_list))

#5-4-2
nations = ['Korea','China','Russia','Malaysia']
print('국가 목록 :', nations)
print('사전에 가장 먼저 나오는 나라 :',min(nations))
print('사전에 가장 뒤에 나오는 나라 :',max(nations))

#5-5-1
a = [1,2,3]
b = [10,20,30]
a.append(b)
print(a)

a = [1,2,3]
b = [10,20,30]
a.extend(b)
print(a)

#5-5-2
nlist = list(range(1,11))
print('nlist =',nlist)

#5-5-3
nlist.insert(0,0)
print('nlist =',nlist)

#5-5-4
nlist.reverse()
print('nlist =',nlist)

#5-5-5
print('마지막 원소 =',nlist.pop())
print('nlist =',nlist)

#5-6
n = int(input('반복할 정수를 입력하시오 :'))
list1 = [1,2,3]
print(list1*n)

n = int(input('반복할 정수를 입력하시오 :'))
print(list1*n)

#5-7-1
nlist = list() # 5-5-2번에서 list를 사용해버렸기 때문에 빈 리스트를 생성함
n_list = list(range(0,15))
print('n_list =',n_list)

#5-7-2
print('s_list1 =',n_list[:5])
print('s_list2 =',n_list[5:11])
print('s_list3 =',n_list[11:])
print('s_list4 =',n_list[2:11:2])
print('s_list5 =',n_list[-5:5:-1])
print('s_list6 =',n_list[-5:0:-2])




