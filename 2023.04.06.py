#range(5) -> 0 ~ 4 (끝값 -1까지)
#range(1, 5) -> 1 ~ 4
#range(1, 10, 2) -> 1, 3, 5, 7, 9 (3번째 수는 간격)

'''
for i in range(1, 6):
    print(i, '환영합니다.')
'''

'''
for name in ['철수', '영희', '길동', '유신']:
    print('안녕!', name)
'''

'''
inputName = input('이름을 입력해주세요: ')
name = ['철수', '영희', '길동', '유신']
for i in name:
    if i == inputName:
        print(inputName + '님 반갑습니다.')
        break
else:
    print('없는 사용자입니다.')
'''

'''
for i in [0, 1, 2, 3, 4, 5]:
    print(i, end="")
print('\n')
for i in [0, 1, 2, 3, 4, 5]:
    print(i, end=" ")
print('\n')
for i in range(0, 6):
    print(i, end=" ")
'''

'''
sum = 0
for i in range(1, 11):
    sum += i
print(sum)
'''

'''
sum = 0
end = int(input('끝값을 입력하세요: '))
for i in range(1, end + 1):
    sum += i
print(sum)
'''

'''
sum = 0
num1, num2 = input('초기값과 끝값을 입력해주세요: ').split()
minNum = min(int(num1), int(num2))
maxNum = max(int(num1), int(num2))
for i in range(minNum, maxNum + 1):
    sum += i
print(sum)
'''

'''
for i in "abcdef":
    print(i, end=" ")
'''

'''
string = input('영어문장을 입력해주세요: ')
consonant = 0
vowel = 0
dot = 0
a = 'aeiouAEIOU'
for i in string:
    if i in a:
        vowel += 1
    elif i == " ":
        continue
    elif i == ".":
        dot += 1
    else:
        consonant += 1
print('자음: ', consonant, '개')
print('모음: ', vowel, '개')
print('점: ', dot, '개')
'''

'''
#공백없이 출력
string = input('영어문장을 입력해주세요: ')
count = 0
for i in string:
    if i == ' ':
        continue
    else:
        count += 1
        print(i, end="")
print('\n글자수:', count)
'''

'''
string = input('영어문장을 입력해주세요: ')
string1 = ''
for i in string:
    if i == ' ':
        continue
    else:
        string1 += i
print(string1)
print('글자수:', len(string1))
'''

'''
#특수문자 지우고 출력
a = '#?^'
string = input('영어문장을 입력해주세요: ')
c = ''
for i in string:
    if i in a:
        c += ''
    else:
        c += i
print(c)
'''

'''
string = input('영어문장을 입력해주세요: ')
for i in string:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z' or i ==' ':
        print(i, end='')
'''

'''
#구구단 출력
for i in range(1, 10):
    print('-'*10, i, '단', '-'*10)
    for j in range(1, 10):
        print(i, '*', j , '=', i * j)
'''

'''
#로또 출력
from random import randint  #randint는 끝값 -1 안되고 끝값까지 된다.
for i in range(1, 8):
    print(str(i) + '일: ', end='')
    for j in range(6):
        print(randint(1, 45), end=' ')
    print('(', randint(1, 45), ')')
    #print('(' + str(randint(1, 45)) + ')')
    print('\n')
'''

 
#로또  같은 번호 출력 안되게 해보기
from random import randint

for i in range(1, 8):
    print(str(i) + '일: ', end='')
    for j in range(6):
        a = []
        b = randint(1, 46)
        for k in range(len(a)):
            if b == a.k:
                b = randint(1, 46)
            else:
                a + b
                break
    for j in a:
        print(a, end='')
    c = randint(1, 46)
    for j in range(len(a)):
            if c == a.k:
                c = randint(1, 46)
            else:
                break
    print('(', c, ')')     #보너스 숫자
    #print('(' + str(randint(1, 45)) + ')')
    print('\n')




#gpt가 수정한거
from random import randint

for i in range(1, 8):
    print(str(i) + '일: ', end='')
    a = []
    for j in range(6):
        b = randint(1, 45)
        while b in a:
            b = randint(1, 45)
        a.append(b)
    a.sort()    # 오름차순 정렬 -> 없어도 됨
    for j in a:
        print(j, end=' ')
    c = randint(1, 45)
    while c in a:
        c = randint(1, 45)
    #print('(' + str(c) + ')')
    print('(%d)' % c) # 보너스 숫자
    print('\n')
