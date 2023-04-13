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

#4장 p.32 자리수의 합
num = int(input('숫자를 넣으세요: '))
sum = 0
while num % 10 != 0:
    sum += num % 10
    num //= 10
print('자리수의 합은', sum, '입니다')
print('자리수의 합은 %d입니다' % sum)