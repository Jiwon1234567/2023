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

a = input('첫 번째 단어를 입력해주세요: ')
b = input('두 번째 단어를 입력해주세요: ')
c = input('세 번째 단어를 입력해주세요: ')
print(a[0].lower() + b[0].lower() + c[0].lower())