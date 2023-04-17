'''
#4장 p.23
i = 0
num = int(input('몇 번을 반복하시겠습니까: '))
while i < num:
    print('환영합니다.')
    i += 1
print('반복이 종료되었습니다.')
'''

'''
#4장 p.24
i = 0
while i < 10:
    print(i, end=' ')
    i += 1
'''

'''
#4장 p.26
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print('합계=', sum)
'''

'''
#초기값과 끝값 받아서 while문으로 더하기
sum = 0
n1, n2 = input('초기값과 끝값을 적어주세요: ').split()
min = min(int(n1), int(n2))
max = max(int(n1), int(n2))
while min <= max:
    sum += min
    min += 1
print('합계= ', sum)
'''

'''
i = 1
sum = 0
while i <= 100:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1
print('1부터 100 사이의 모든 3, 5의 배수의 합은', sum, '입니다')
print('1부터 100 사이의 모든 3, 5의 배수의 합은 %d입니다' % sum)
'''

'''
i = 1
sum = 0
max = int(input('끝 값을 적어주세요: '))
multi = int(input('배수를 적어주세요: '))
while i <= max:
    if i % multi == 0:
        sum += i
    i += 1
print('1부터', max, '사이의 모든', multi,'의 배수의 합은',sum,'입니다.')
'''

'''
#4장 p.32 자리수의 합
num = int(input('숫자를 넣으세요: '))
sum = 0
while num % 10 != 0:
    sum += num % 10
    num //= 10
print('자리수의 합은', sum, '입니다')
print('자리수의 합은 %d입니다' % sum)
'''

'''
#4장 p.35
print('종료하려면 음수를 입력하시오')
num = 1
sum = 0
count = 0
while num > 0:
    num = int(input('성적을 입력하시오: '))
    if num > 0:
        sum += num
        count += 1
if count > 0:
    avg = sum / count
print('성적의 평균은', avg,'입니다.')
'''

'''
for i in range(5):
    for j in range(10):
        print('*', end='')
    print('')
'''

'''
for i in range(5):
    for j in range(10-i):
        print('*',end='')
    print('')
'''

'''
s = input('문자열을 입력하시오: ')
vowels = 'aeiouAEIOU'
result =''
for letter in s:
    if letter not in vowels:
        result += letter
print(result)
'''

'''
s = input('문자열을 입력하시오: ')
s = s.lower()   #.upper() 소문자 -> 대문자
vowels = 'aeiou'
result =''
for letter in s:
    if letter not in vowels:
        result += letter
print(result)
'''

'''
#4장 p.47
original = input('문자열을 입력하세요: ')
word = original.lower()
vowels = 0
consonants = 0
space = 0
digit = 0

if len(original) > 0:
    for char in word:
        if char in 'aeiou':
            vowels += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            digit += 1
        else:
            consonants += 1
            
print('모음의 개수:', vowels)
print('자음의 개수:', consonants)
print('간격의 개수:', space)
print('숫자의 개수:', digit)
'''

'''
#4장 p.48
s = input('문자열를 입력하시오: ')
alpha = 0
digit = 0
space = 0
if len(s) > 0:
    for i in s:
        if i.isalpha():
            alpha += 1
        elif i.isdigit():
            digit += 1
        elif i.isspace():
            space += 1
print('알파벳의 개수:', alpha)
print('간격의 개수:', space)
print('숫자의 개수:', digit)
'''

num = input('계좌번호를 입력하시오: ')
s = ''
if len(num) > 0:
    for i in num:
        if i == '-':
            continue
        else:
            s += i
print('계좌번호:', s)