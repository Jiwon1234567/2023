def print_menu():
    print('-'*20)
    print('1. 친구 리스트 출력')
    print('2. 친구추가')
    print('3. 친구삭제')
    print('4. 이름변경')
    print('9. 종료')

friend = []
#menu = 5
while True:
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