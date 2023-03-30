'''
#p25 놀이기구 타는 조건
age, height = input('나이와 키를 입력하세요.').split()  #split은 문자열로만 받을 수 있음
if int(age) >= 10 and int(height) >= 160:
    print('놀이기구를 탈 수 있습니다.')
elif int(age) >= 10 or int(height) >= 160:
    print('아쉽군요')
else:
    print('놀이기구를 탈 수 없습니다.')
'''

'''
#p.26 졸업 학점 검사하기
num, grade = input('이수한 학점수와, 평점을 입력하시오').split()
if int(num) >= 140 and float(grade) >= 2.0:
    print('졸업가능합니다.')
elif int(num) >= 140 or float(grade) >= 2.0:
    print('졸업이 힘듭니다.')
else:
    print('졸업할 수 없습니다,')
'''

'''
#p.29 연속적인 if-else문
grade = int(input('학점을 입력하세요: '))
if 0 <= grade <= 100:
    if grade >= 90:
        print(str(grade) + '점 학점은 A')
    elif grade >= 80:
        print(str(grade) + '점 학점은 B')
    elif grade >= 70:
        print(str(grade) + '점 학점은 C')
    elif grade >= 60:
        print(str(grade) + '점 학점은 D')
    else:
        print(str(grade) + '점 학점은 F')
else:
    print('잘못 입력하셨습니다.')
'''

'''
#p.31 음수, 0, 양수 구별하기
#프로그래밍 기법 고려 -> 제일 많이 나오는걸 if문 제일 위에 두기 -> 속도가 빠르다
num = int(input('정수를 입력하시오: '))
if num > 0 :
    print('입력된 정수는 양수입니다.')
elif num < 0:
    print('입력된 정수는 음수입니다.')
else:
    print('입력된 정수는 0입니다.')
'''

'''
#p.35 사과 구입 
quality = input('사과의 상태를 입력하시오: ')
if quality == '신선':
    price = int(input('사과 1개의 가격을 입력하시오: '))
    if price >= 1000:
        print('사지 않는다')
    else:
        money = int(input('가지고 있는 돈은 얼마입니까: '))
        print(money // price, '개를 산다')
else:
    print('사과를 사지 않는다.')
'''

'''
#p.38 아이디 검사
list = ['hong', 'lee', 'kang']

id = input('아이디: ')
if id in list:
    pw = input('패스워드: ')
    if pw == '1234567':
        print('환영합니다.')
    else:
        print('잘못된 패스워드입니다.')
else:
    print('알 수 없는 사용자입니다')
'''

'''
#p.40 달의 일수 입력
thiryone = [1, 3, 5, 7, 8, 10, 12]
month = int(input('월을 입력하시오: '))
if month == 2:
    print(str(month) +'월의 날수는 28')
elif month in thiryone:
    print(str(month) + '월의 날수는 31')
else:
    print(str(month) + '월의 날수는 30')
'''

'''
#p.42 윤년 판단
year = int(input('연도를 입력하시오: '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(str(year) + "년은 윤년입니다.")
else:
    print(str(year) + '년은 윤년이 아닙니다.')
'''

'''
#문자로 받은거 완전히 숫자로 바꾸는거
a = "100"
a = int(a)
'''

'''
import random #모든 random함수를 다 가져옴
a = random.randint()

from random import * #모든 random함수를 다 가져오는건 똑같은데 random.을 안적어줘도됨
a = randint()

from random import randint #함수 하나만 가져오는거(가장 많이 쓴다)
a = randint()
'''

'''
#p.46 숫자 맞추기 게임
print('숫자 게임에 오신 것을 환영합니다.')
from random import randint
answerNum = randint(1, 100)
inputNum = int(input('숫자를 맞춰 보세요: '))
if inputNum == answerNum:
    print('정답입니다.')
elif inputNum > answerNum:
    print('너무 큼')
else:
    print('너무 작음')
print('게임 종료')
'''


from random import randint
player = input('가위, 바위, 보 중에서 하나를 선택하세요: ')
num = randint(0, 2)
if num == 0:
    computer = "가위"
elif num == 1:
    computer = "바위"
else:
    computer = "보"

print('사용자: ' + player, '/ 컴퓨터: ' + computer)
if computer == player:
    print('비겼음')
elif (computer == "바위" and player == "가위") or (computer == "가위" and player == "보") or (computer == "보" and player == "바위"):
    print('졌음')
else:
    print('이겼음')