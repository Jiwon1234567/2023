#6장
#리스트 문제 기말고사에 몇개 나옴

'''
#p.2
a = [10, 20, 30]
a[0] = 40
#a[3] = 50 -> 안됨
a.append(50)
print(a)
'''

'''
#p.4
scores = []     #리스트는 만들어주고 써야됨
for i in range(5):
    a = int(input('성적을 입력하시오: '))
    scores.append(a)
print(scores)
'''

'''
#p.6
scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]

scores[0] = 80
scores[1] = scores[0]

for i in range(10):
    scores[i] = 10  #만들어져 있으면 대입문 쓸 수 있다
'''


'''
#p.7
scores = [32, 56, 64, 72, 12, 37, 98, 77, 59, 69]

for element in scores:
    print(element, end=' ')
'''

'''
#p.8
list1 = list()  #함수를 이용하여 만드는 방법
list1 = []      #리스트를 이용하여 만드는 방법  #두 개 같은 의미

list2 = list('Hello')
list2 = ['H', 'e', 'l', 'l', 'o']   #두 개 같은 의미

list3 = list(range(0, 5))
list3 = [0, 1, 2, 3, 4]        #두 개 같은 의미

print(list1)    #리스트를 그대로 출력하면 리스트 형식 그대로 [ , ] 도 같이 출력 됨
print(list2)
print(list3)
'''

'''
#p.9
list1 = [12, 'dog', 180.14]
list2 = [['Seoul', 10], ['Paris', 12], ['London', 50]]

print(list2[0])
print(list2[1])
print(list2[1][1])

for i in range(3):
    print(list2[i][0])
    print(list2[i][1])
'''

'''
#p.9
scores = []
sum = 0
count = 0
for i in range(5):
    scores.append(int(input('성적을 입력하시오: ')))

for i in scores:    #for i in range()쓰지 말기
    sum += i
    if i >= 80:
        count += 1

print('성적 평균은', sum/5, '입니다.')
print('80점 이상 성적을 받은 학생은 %d명 입니다.' %count)
'''

'''
#p.10 성적 처리 프로그램
scores = []
count = 0

for i in range(5):
    score = int(input('성적을 입력하시오: '))
    scores.append(score)
    if score >= 80:
        count += 1
    
sum = 0

for i in scores:
    sum += i

avg = sum / len(scores)
print('성적 평균은', avg, '입니다.')
print('80점 이상 성적을 받은 학생은 %d명입니다.'%count)
'''



'''
#p.12
dogNames = []
while True:
    name = input('강아지의 이름을 입력하시오(종료시에는 엔터키) ')
    if name == '':  #따음표 두 개 붙여야 엔터키(띄워놓으면 스페이스키가 됨)
        break
    dogNames.append(name)

print('강아지들의 이름: ')
for i in dogNames:
    print(i, end=', ')
'''

'''
#슬라이싱
text = 'Hello.txt'
print(text[0:3])    #Hel
print(text[1:])     #ello.txt
print(text[-3:])    #txt
'''

'''
values = [1, 2, 3] * 3
print(values)
'''

'''
#p.20
marvel_heroes = ['스파이더맨', '헐크', '아이언맨']
dc_heroes = ['슈퍼맨', '배트맨', '원더우먼']
heroes = marvel_heroes + dc_heroes
print(heroes)
print(len(heroes))
heroes.append('그루트')
print(heroes)
'''

'''
heroes = ['스파이더맨', '헐크', '아이언맨', '슈퍼맨', '배트맨', '원더우먼']
a = input('이름을 입력하세요: ')
if a in heroes:
    print(a + '는 영웅입니다.')
else:
    print(a + '는 영웅이 아닙니다.')
'''

'''
heroes = ['스파이더맨', '헐크', '아이언맨', '슈퍼맨', '배트맨', '원더우먼']
a = heroes.index('스파이더맨')
print(a)
'''

'''
heroes = ['스파이더맨', '헐크', '아이언맨', '슈퍼맨', '배트맨', '원더우먼']
a = heroes.index('스파이더맨')
heroes.pop(a)   #인덱스로 지우는법(pop)
heroes.remove('헐크')   #이름으로 지우는법(remove)
print(heroes)
'''

'''
a = [3, 2, 1, 5, 4]
a.sort()
print(a)

b = [3, 2, 1, 6, 5]
c = sorted(b)   #sorted함수는 원본은 그대로 놔두고 정렬된 새로운 리스트를 만듦
print(b)
print(c)
'''
#sort 함수랑 sorted 함수 구분 중요


'''
scores = [10, 20, 30, 40, 50]
values1 = scores                 #얕은 복사
values2 = list(scores)           #깊은 복사

print(scores)
scores[2] = 99
print('얕은 복사:' ,values1)
print('깊은 복사:', values2)
'''


#7장
'''
t1 = (1, 2, 3, 4, 5)    #()를 쓰면 튜플
t1[0] = 100         #튜플은 변경 불가능 -> 에러뜸
'''


'''
student = ('철수', 19, 'CS')
(name, age, major) = student
print(name)
print(age)
print(major)
'''

'''
numbers = {2, 1, 3}     #세트는 방 번호가 없어서 인덱스 지원 안함, 작은 숫자부터 출력됨(슬라이싱도 안됨)
print(numbers)
numbers.add(4)          #세트(집합)에 추가 할 땐 append가 아니고 add를 사용

for x in numbers:
    print(x, end=' ')
'''

'''
A = {1, 2, 3, 4, 5}
B = {1, 2, 3}
B.issubset(A)   #B가 A의 subset(포함되어있는가)
'''


#!!!!!!!!!!!!!tuple, set 시험에 안나옴!!!!!!!!!!!!!!!


#!!!!!!!!!!!!!!!딕셔너리 제일 중요함!!!!!!!!!!!!!!!!

'''
#딕셔너리는 {}안에 'key':'value'로 이루어져 있다
#key로만 접근 가능
dic = {'Kim':'12312412', 'Park':'010129391'}
#print(dic[0]) -> 딕셔너리는 []안에 index가 들어가는게 아니라 key가 들어가야됨
print(dic['Kim'])   #key를 넣으면 value가 나온다
print(dic.get('Kim')) #get('key')함수를 써도 똑같다(취향차이, 헷갈리니까 하나만 쓰기)
'''

'''
dic = {'Kim':'12312412', 'Lee':'010129391'}
dic['Park'] = '1231248322'  #딕셔너리 항목 추가 방법
print(dic)
dic['Lee'] = '23942402938'    #이미 있는것은 변경이 됨
'''

'''
a = {}  #새로운 딕셔너리 만드는법(초기화)
a = dict()  #새로운 딕셔너리 만드는 함수(위에껀 헷갈려서 이걸 사용하는게 좋음)
a['Lee'] = 123124
a['Park'] = 123124
print(a['Lee'])
'''


contacts = {'Kim':'12312412', 'Lee':'010129391'}
contacts.pop('Kim')     #key를 주면 항목이 삭제됨
print(contacts)