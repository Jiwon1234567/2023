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
#문제 1 수정(%f, 길이만을 구하는 함수)
from math import sqrt

def distance(a1, b1, a2, b2):
    distance = sqrt((int(a2) - int(a1)) ** 2 + (int(b2) - int(b1)) ** 2)
    return distance

x1, y1 = input('한점을 입력하세요: ').split()
x2, y2 = input('다른 한점을 입력하세요: ').split()

d = distance(x1, y1, x2, y2)
print('('+ x1 + ',' + y1 + ')과 (' + x2 + ',' + y2 + ')의 길이는 %f입니다.' %d)     #결과가 소수로 나올 수 있으므로 %f
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

'''
def calculator():
    a, sign, b = input('사칙연산을 위한 정수와 기호를 넣어주세요: (예: 3 + 4): ').split()
    
    if sign == '+':
        print(a, sign, b, '=', int(a) + int(b))
    elif sign == '-':
        print(a, sign, b, '=', int(a) - int(b))
    elif sign == '*':
        print(a, sign, b, '=', int(a) * int(b))
    elif sign == '/':
        print(a, sign, b, '=', int(a) / int(b))
    else:
        print('잘못 입력하셨습니다.')
        
calculator()
'''



'''
#문제 3
#문자열(파이썬)과 횟수(3)를! 매개변수로 전달받아
def print_str(string, repeat):
    for i in range(repeat):
        print(string)

string = input('문자열: ')
repeat = int(input('\n횟수: '))
print_str(string, repeat)
'''

'''
#5월 25일 과제
def print_menu():
    print('-'*20)
    print('1. 친구 리스트 출력')
    print('2. 친구추가')
    print('3. 친구삭제')
    print('4. 이름변경')
    print('9. 종료')

friend = []
menu = 5
while menu != 9:
    print_menu()
    menu = int(input('메뉴를 선택하시오: '))
    if menu == 1:
        print(friend)
    elif menu == 2:
        friend_name = input('이름을 입력하시오: ')
        friend.append(friend_name)
    elif menu == 3:
        friend_name = input('이름을 입력하시오: ')
        friend.remove(friend_name)
    elif menu == 4:
        friend_name = input('이름을 입력하시오: ')
        replace = friend.index(friend_name)
        new_name = input('새로운 이름을 입력하시오: ')
        friend[replace] = new_name
    elif menu == 9:
        break
    else:
        print('잘못 입력하셨습니다.')
'''



'''
#6/1과제
def print_menu():
        print('1.연락처 추가')
        print('2.연락처 삭제')
        print('3.연락처 검색')
        print('4.연락처 출력')
        print('5.종료')

contact = dict()
while True:
    print_menu()
    menu = int(input('메뉴 항목을 선택하시오: '))
    if menu == 1:
        name = input('이름: ')
        number = input('전화번호: ')
        contact[name] = number
    elif menu == 2:
        name = input('삭제할 이름: ')
        contact.pop(name)
    elif menu == 3:
        name = input('검색(이름): ')
        number = contact[name]
        print(name + '의 전화번호:', number)
    elif menu == 4:
        for i in contact:
            print(i + '의 전화번호:', contact[i])
    elif menu == 5:
        break
    else:
        print('잘못 입력하셨습니다.')
    print('-'*30)
'''