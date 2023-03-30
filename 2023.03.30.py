#p25 놀이기구 타는 조건
age, height = input('나이와 키를 입력하세요.').split()  #split은 문자열로만 받을 수 있음
if int(age) >= 10 and int(height) >= 160:
    print('놀이기구를 탈 수 있습니다.')
else:
    print('놀이기구를 탈 수 없습니다.')