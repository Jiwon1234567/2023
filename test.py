def select_num(menu = 2):
    if menu == 1:
        return 1
    elif menu == 2:
        return 2
    else:
        print('잘못 입력하셨습니다')

n = int(input('select num: '))
print(select_num())