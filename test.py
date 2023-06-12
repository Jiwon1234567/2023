def calculator():
    a, sign, b = input('사칙연산을 위한 정수와 기호를 넣어주세요: (예: 3 + 4): ').split()
    
    if sign == '+':
        print(a, sign, b, '=', int(a) + int(b))
    elif sign == '-':
        print(a, sign, b, '=', int(a) - int(b))
    elif sign == '*':
        print(a, '*', b, '=', int(a) * int(b))
    elif sign == '/':
        print(a, '/', b, '=', int(a) / int(b))
    else:
        print('잘못 입력하셨습니다.')
        
calculator()