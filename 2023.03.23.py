'''
#대화하는 프로그램 만들기
price = int(input('물건값을 입력하시오: '))
thousands= int(input('1000원 지폐개수: '))
fivehun = int(input('500원 동전개수: '))
hundreds = int(input('100원 동전개수: '))

receive = thousands * 1000 + fivehun * 500 + hundreds * 100
change = receive - price


change500 = change // 500
change100 = (change % 500) // 100
change50 = (change % 100) // 50
change10 = (change % 50) // 10
change1 = (change % 10) // 1

print('500원=', change500, ', 100원=', change100, ', 50원=', change50, ', 10원=', change10, ', 1원=', change1)
'''

'''
a = 'Hello.exe'
print(a, a[0], a[0:4], a[-1])
print(a[2:])
print(a[-3:])   #확장자만 뽑을 때

a = '"hello.exe"'
print(a)
b = "'hello.exe'"
print(b)
'''

'''
line = "=" * 50
print(line)
'''

'''
a = input('첫 번째 단어를 입력해주세요: ')
b = input('두 번째 단어를 입력해주세요: ')
c = input('세 번째 단어를 입력해주세요: ')
a.upper()
b.upper()
c.upper()
print(a[0] + b[0] + c[0])
'''

'''
a = input('첫 번째 단어를 입력해주세요: ')
b = input('두 번째 단어를 입력해주세요: ')
c = input('세 번째 단어를 입력해주세요: ')
print(a[0].lower() + b[0].lower() + c[0].lower())
'''

'''
a, b, c = input("정수 두개: ").split() #split는 문자열로만 받을 수 있다
print(int(a) + int(b) + int(c))  #int로 하나씩 일일이 바꿔줘야됨
'''

'''
a, b, c = input('단어 세개를 입력해주세요: ').split()
print(a[0].upper() + b[0].upper() + c[0].upper())
'''

'''
age, name = input('나이와 이름을 입력해주세요 ').split()
print(name +'님 10년 후 나이는', int(age) + 10,'입니다')
'''

'''
age, name = input('나이와 이름을 입력해주세요 ').split()
print(name +'님 10년 후 나이는', int(age) + 10, end="")
print('입니다')
'''

'''
score = int(input('점수를 입력하세요: '))
if score >= 60:
    print('합격입니다.')
else:
    print('불합격입니다.')
'''

#3장 선택

'''
food = '스테이크'
if food == '스테이크':
    print('내가 제일 좋아하는 음식!')
    print(10 * food)
'''

'''
food = ['스테이크', '불고기', '햄버거', '치킨']
you = input('좋아하는 음식은 무엇입니까? ')

if you in food:
    print('취향이 같군요')
else:
    print('취향이 다르군요')
'''

'''
weight = float(input('짐의 무게는 얼마입니까? '))
if weight < 21:
    print('짐에 대한 수수료는 없습니다.')
else:
    print('무거운 짐은 20,000원을 내셔야 합니다.')
print('감사합니다.')
'''

'''
num = int(input('정수를 입력하시오: '))
if num % 2 == 0:
    print('입력된 정수는 짝수입니다.')
else:
    print('입력된 정수는 홀수입니다.')
'''

'''
n1, n2 = input('두 개의 정수를 입력해주세요: ').split()
if int(n1) > int(n2):
    print('큰 수는', n1)
else:
    print('큰 수는', n2)
'''

'''
price = int(input('구입금액을 입력하세요: '))
if price >= 100000:
    print('지불금액:', int(price * 0.95))
else:
    print('지불금액:', price)
'''

string = input('문자열을 입력하시오: ')
l = len(string)
k = l // 2
length = len(string)
if length % 2 == 0:
    print(string[k-1] + string[k])
else:
    print(string[k])