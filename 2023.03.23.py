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