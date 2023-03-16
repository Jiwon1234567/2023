'''
s = 1
s = s + 1
print(s)
'''

'''
if "사과" in ["딸기", "바나나", "포도", "사과"]:
    print("사과가 있습니다")
    print("good")
'''

'''
a = '안녕'
b = '하세요'
c = a + b
d = 1
print(c, d) #콤마(,) 쓰면 한칸이 띄워진다. 붙이려면 문자열을 더하기 연산자로 써야됨
print(c, end="") #end="" or end='' 쓰면 붙여진다
print(d)
print(a + b, '\n반갑습니다') #\n쓰면 줄 띄워짐
print(a + b, end="")
print('반갑습니다')
'''

'''
print("결과값은", 2 * 7, "입니다.") #문자열과 숫자는 더하기 연산자 안된다.
print("결과값은", 2 * 7, end='')
print('입니다')
'''

'''
#원 넓이 구하기
#r = 5
r = float(input('반지름을 입력하세요: '))     #input 함수는 default가 str형태이다
PI = 3.14   #나중에도 안바꿀거면 대문자로 선언
area = r * r * PI
print('반지름이', r, '인 원의 넓이는', area, '입니다')
area2 = r ** 2 * PI     # **는 승을 나타냄(ex 2 ** 2 = 2의 2승)
print('반지름이', r, '인 원의 넓이는', area2, '입니다')
print('반지름이', str(r) + '인 원의 넓이는', area, '입니다')     #str(?)로 쓰면 이 순간에만 str로 바꾸는 거 (캐스트 연산자?) -> str로 바꿔서 더하기 연산자 사용해서 붙여서 쓸 수 있다
print(type(r))
'''

'''
#삼각형 넓이 구하기
l = float(input('밑변을 입력하세요: '))
h = float(input('높이를 입력하세요: '))
area = l * h / 2
print('밑변', l, '높이', h, '인 삼각형의 넓이는', area, '이다')
'''

'''
#39페이지 한줄로 출력
print("안녕하세요? 여러분\n저는 파이썬을 무척 좋아합니다.\n9*8은", 9 * 8, "입니다.\n안녕히 계세요.")
'''

'''
name = input('이름: ')
age = int(input('나이: '))
print('이름은 ' + name + '이고 나이는', age, '이다')
'''

'''
#candy = 120
candy = int(input('사탕 가격: '))
money = int(input('현재 가지고 있는 금액은 얼마입니까? '))
print('사탕의 개수:', money // candy, '\n잔액:', money % candy) #나눠서 정수부분만 나타내려면 //쓰면됨
'''

'''
r = float(input('반지름: '))     #산술연산할때 조건 없으면 float을 기본으로 사용
PI = 3.14
print('반지름이', r, '인 구의 부피는', 4 / 3 * PI * r ** 3, '이다')
'''

'''
name = input('이름이 무엇입니까: ')
print(name + '님 반갑습니다')
age = int(input('나이는 얼마인가요: '))
if age < 30 and age > 0:        # &&써도 되는데 and 써주는게 정통임, 0 < age < 30도 사용가능(좋진 않음)
    print(30-age, '년 후면 30살이 되시는군요')
else:
    print('이미 30이 넘으셨군요 할아방탱이네요')
'''

'''
num = int(input('참석자의 수를 입력하시오: '))
print('치킨의 수:', num, '\n맥주의 수:', num * 2, '\n케익의 수:', num * 4)
'''