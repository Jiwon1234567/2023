num = int(input('숫자를 넣으세요: '))
sum = 0
while num > 0:            #조건 중요???? num > 0
    sum += num % 10
    num //= 10
print('자리수의 합은', sum, '입니다')
print('자리수의 합은 %d입니다' % sum)