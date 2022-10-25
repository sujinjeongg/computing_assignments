
#8-1
try:
    a = [10,20,30]
    print(a[3])
except Exception as e:
    print('error:',e)

try:
    n = int('20%')
except Exception as e:
    print('error:',e)

try:
    a = 100 + '200'
except Exception as e:
    print('error:',e)

#8-2
try:
    10*(30/0)
except ZeroDivisionError:
    print('0으로 나누는 오류 발생')
except ValueError:
    print('입력 값이 정수나 실수가 아닙니다.')
except Exception as e:
    print('error:',e)

try:
    x = int(input('정수 x를 입력하세요:'))
except ZeroDivisionError:
    print('0으로 나누는 오류 발생')
except ValueError:
    print('입력 값이 정수나 실수가 아닙니다.')
except Exception as e:
    print('error:',e)
else:
    print('수행에 성공했습니다.')

try:
    import sys
    f = open('myfile.txt')
    s = f.readline()
except ZeroDivisionError:
    print('0으로 나누는 오류 발생')
except ValueError:
    print('입력 값이 정수나 실수가 아닙니다.')
except FileNotFoundError:
    print('파일을 찾지 못했습니다.')
except Exception as e:
    print('error:',e)
else:
    f = open('myfile.txt')
    s = f.readline()    

#8-3
a = [1,2,3,4,5]
try:
    element = input('a의 요소를 하나 선택하시오 :')
    result = int(element)
except ValueError:
    print('오류 : 입력 값이 정수나 실수가 아님')
except Exception as e:
    print('error:',e)
else:
    if (result == a[0]):
        print(result,'는 첫 번째 요소입니다.')
    elif (result == a[1]):
        print(result,'는 두 번째 요소입니다.')
    elif (result == a[2]):
        print(result, '는 세 번째 요소입니다.')
    elif (result == a[3]):
        print(result, '는 네 번째 요소입니다.')
    elif (result == a[4]):
        print(result, '는 다섯 번째 요소입니다.')

#8-4
f = open('numbers.txt','w')
k = 100
for i in range(4):
    f.write('{}\n'.format(k))
    k+=100
f.close()

f = open('we_will_rock.txt','w')
f.write('Buddy, you\'re a boy, make a big noise\n')
f.write('Playing in the street, gonna be a big man someday\n')
f.write('You got mud on your face, you big disgrace\n')
f.write('Kicking your can all over the place, singin\'\n')
f.write('We will, we will rock you\n')
f.write('We will, we will rock you\n')
f.close()

#8-5
f = open('numbers.txt','w')
k = 100
for i in range(4):
    f.write('{}\n'.format(k))
    k += 100
f.close()
f = open('numbers.txt','r')
for i in range(4):
    s = f.readline().rstrip()
    print(s)
f.close()

f = open('we_will_rock.txt','r')
for i in range(6):
    s = f.readline().rstrip()
    print(s)

#8-6-1
f = open('we_will_rock.txt','w')
f.write('Buddy, you\'re a boy, make a big noise\n')
f.write('Playing in the street, gonna be a big man someday\n')
f.write('You got mud on your face, you big disgrace\n')
f.write('Kicking your can all over the place, singin\'\n')
f.write('We will, we will rock you\n')
f.write('We will, we will rock you\n')
f.close()

fname = input('입력할 파일의 이름:')
f = open(fname, 'r')
s = f.readline().rstrip().upper()
for i in range(6):
    print(s)
    s = f.readline().rstrip().upper()

f.seek(0)
fp = open('we_will_rock_upper.txt', 'w')
s = f.readline().rstrip().upper()
for i in range(6):
    fp.write(s)
    fp.write('\n')
    s = f.readline().rstrip().upper()
f.close()
fp.close()

#8-6-2
f = open('we_will_rock.txt','w')
f.write('Buddy, you\'re a boy, make a big noise\n')
f.write('Playing in the street, gonna be a big man someday\n')
f.write('You got mud on your face, you big disgrace\n')
f.write('Kicking your can all over the place, singin\'\n')
f.write('We will, we will rock you\n')
f.write('We will, we will rock you\n')
f.close()

fname = input('입력할 파일의 이름:')
f = open(fname, 'r')
listr = []

for i in range(6):
    s = f.readline().rstrip()
    listr.append(s)
for i in range(6):
    print(listr[6 - (i+1)])

#추가 시험에 나올 것 같은 예제 p.500 8-18
fname = input('입력할 파일의 이름 :')
f = open(fname, 'r')
n = 1
l = f.readline()
while l:
    print('{:3d}: {}'.format(n,l), end = '')
    n += 1
    l = f.readline()
f.close()

#추가 시험에 나올 것 같은 예제 p.508 8-24
import sys

success = False
try:
    fname = input('입력 파일명 ')
    with open(fname, 'r', encoding = 'UTF8') as f:
        n = 1
        l = f.readline()
        while l:
            print('{:3d}: {}'.format(n,l), end ='')
            n += 1
            l = f.readline()
        success = True
except IOError:
    print('Could not read file:', fname)
except:
    print('Unexpected error:', sys.exc_info()[0])

print('file access successful? ',success)    

