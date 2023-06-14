contact = {}
while True:
    print('1.연락처 추가')
    print('2.연락처 삭제')
    print('3.연락처 검색')
    print('4.연락처 출력')
    print('5.종료')
    
    menu = int(input('메뉴 항목을 선택하시오: '))
    if menu == 1:
        name = input('이름:')
        num = input('전화번호:')
        contact[name] = num
    elif menu == 2:
        name = input('이름:')
        contact.pop(name)
    elif menu == 3:
        name = input('이름:')
        num = contact[name]
        print(name,'의 전화번호:',num)
    elif menu == 4:
        for i in contact:
            print(i,'의 전화번호:',contact[i])
    elif menu == 5:
        break
