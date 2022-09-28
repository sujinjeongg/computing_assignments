#5-3
list1 = [3,5,7]
list2 = [2,3,4,5,6]
for i in list1:
    for n in list2:
        print(i,'*',n,'=',i*n)

#5-4
a = [2,3,4,5,6]
print('a =',a)
rev_a = list(range(5))
for i in range(0,5):
    rev_a[i] = a.pop(4 - i)
    i += 1
print('rev_a =',rev_a)

#5-7
n_list = [10,20,30,50,60]
print('리스트 원소들 :',n_list)
listsum = 0
for i in n_list:
    listsum += i
print('리스트 원소들의 합 :',listsum)

#5-9
n_list = [10,20,30,50,60]
print('리스트 원소들 :',n_list)
listmax = n_list[0]
for i in range(len(n_list)):
    if n_list[i] > n_list[i-1]:
        listmax = n_list[i]
    else:
        listmax = n_list[i-1]
print('리스트 원소들 중 최댓값 :',listmax)

#5-11
one,two,three,four,five = map(int,input('5개의 수를 입력하세요:').split())
n_list = []
n_list = [one,two,three,four,five]
print('합 :',sum(n_list))
print('평균 :',sum(n_list) / len(n_list))
print('최댓값 :',max(n_list))
print('최솟값 :',min(n_list))


        
