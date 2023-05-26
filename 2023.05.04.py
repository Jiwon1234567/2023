'''
#파이썬은 Return 여러개 가능
def sum(a, b):
    return a, b

print(sum(c, d))
'''

'''
#5장 p.7
def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum, i

value, a = get_sum(1, 10)
print(value, a)
'''

'''
#5장 p.13
def square(n):
    return n * n
print(square(10))
'''



'''
def get_max_min(x, y):
    Max = max(x, y)     #함수 안에서는 함수명 겹치면 안됨 변수명으로 min, max 사용 불가
    Min = min(x, y)
    return Max, Min

def main():
    m, n = get_max_min(3, 10)
    print('큰 값: %d' % m, '작은 값: %d' % n)

main()
'''



'''
def get_max_min(x, y):
    Max = max(x, y)
    Min = min(x, y)
    return Max, Min

def main():
    a, b = input('두 수를 넣어주세요: ').split()
    m, n = get_max_min(int(a), int(b))
    print('큰 값: %d' % m, '작은 값: %d' % n)

main()
'''


'''
def get_max_min(a, b, c, d):
    Max = max(a, b, c, d)
    Min = min(a, b, c, d)
    return Max, Min

def main():
    n1, n2, n3, n4 = input('네 개의 수를 넣어주세요: ').split()
    m, n = get_max_min(int(n1), int(n2), int(n3), int(n4))
    print('큰 값: %d' % m, '/ 작은 값: %d' % n)
    
main()
'''

'''
#5장 p.17
def power(a, b):
    value = 1
    for i in range(b):
        value *= a
    return value

print(power(3, 2))
'''

'''
#5장 p.23
def is_prime(n):
    for i in range(n):
        if i % n == 0:
            return False
    return True

n = int(input('정수를 입력하시오: '))
print(is_prime(n))
'''


'''
#5장 p.27
import math
def sphereVolumeArea(r, menu):
    if menu == 1:
        return 4 / 3 * math.pi * r ** 3
    elif menu == 2:
        return 2 * math.pi * r
    else:
        print('잘못 입력하셨습니다')

r = float(input('구의 반지름을 입력하시오: '))
menu = int(input('부피는 1번, 면적은 2번을 넣어주세요:  '))
if menu == 1:
    print('부피는:', sphereVolumeArea(r, menu))
else:
    print('면적은:', sphereVolumeArea(r, menu))
'''



'''
#5장 p.29 !!!!!!중요한 문제!!!!!!!!
import random
#from random import randrange -> randrange(len(alphabet))

def genPass():
    alphabet = 'abcdefghijklmnopqrstuwxyz0123456789'
    password = ''
    
    for i in range(6):
        index = random.randrange(len(alphabet))
        password += alphabet[index]
    
    return password

print(genPass())
print(genPass())
print(genPass())
'''

'''
#default 인수 -> 값을 미리 정해주는 것
def select_num(menu = 2):
    if menu == 1:
        return 1
    elif menu == 2:
        return 2
    else:
        print('잘못 입력하셨습니다')

n = int(input('select num: '))
print(select_num(n))
'''

'''
#p.33
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

#default인수 안써도 됨
r1 = mul(a = 20, b = 30)
r2 = add(a = 10, b = r1)
print(r2)

r3 = add(10, mul(20, 30))
print(r3)
'''

'''
#전역변수 사용 예
width = 10
height = 20

def area():
    area = width * height
    return area

print(area())
'''

'''
#보통은 이렇게 씀(전역변수 -> 지역변수)
#전역변수는 바뀌면 안되는 값인데 함수에서 사용하다가 바껴버릴수 있기 때문에 항상 전역변수를 지역변수로 받아서 사용하는게 좋다
width = 10
height = 20

def area(w, h):
    area = w * h
    return area

print(area(width, height))
'''

'''
def sub():
    global s
    
    print(s)
    s = '바나나가 좋음!'
    print(s)
    
s = '사과가 좋음!'
sub()
print(s)
'''

#p.40 머리로 풀어보기

