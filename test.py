'''
#문제 1
from math import sqrt

def print_distance(a1, b1, a2, b2):
    distance = sqrt((int(a2) - int(a1)) ** 2 + (int(b2) - int(b1)) ** 2)
    print('('+ a1 + ',' + b1 + ')과 (' + a2 + ',' + b2 +')의 길이는 %d입니다.' % distance)

x1, y1 = input('한점을 입력하세요: ').split()
x2, y2 = input('다른 한점을 입력하세요: ').split()

print_distance(x1, y1, x2, y2)
'''

'''
#문제 2
def calculator():
    a, sign, b = input('사칙연산을 위한 정수와 기호를 넣어주세요: (예: 3 + 4): ').split()
    
    if sign == '+':
        print(a, '+', b, '=', int(a) + int(b))
    elif sign == '-':
        print(a, '-', b, '=', int(a) - int(b))
    elif sign == '*':
        print(a, '*', b, '=', int(a) * int(b))
    elif sign == '/':
        print(a, '/', b, '=', int(a) / int(b))
    else:
        print('잘못 입력하셨습니다.')

calculator()
calculator()
'''


#문제 3
def print_str():
    string = input('문자열: ')
    print()
    
    repeat = int(input('횟수: '))
    
    for i in range(repeat):
        print(string)

print_str()