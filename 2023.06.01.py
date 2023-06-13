#7장 21페이지 딕셔너리 생성부터

'''
#딕셔너리 생성 방법
a = {}          #초기화 할 땐 사용하면 편함
a = dict()      #이 방법을 더 선호함

contacts = {'Kim':'012345678', 'Park':'010123566', 'Lee':'10130392329'}
print(contacts['Kim'])
print(contacts.get('Lee'))

contacts['Choi'] = '01238712498'    #기본적으로 맨 뒤에 추가되지만 딕셔너리는 key로 접근하기 때문에 순서는 상관없음
print(contacts)
contacts.pop('Kim')
print(contacts)
'''

'''
score = {'Korean':80, 'Math':90, 'English':70}
print(score)
for i in score.items():     #.items()쓰면 value까지 같이 나온다(잘 안씀)
    print(i)
for i in score:             #i에 key가 들어간다
    print(i)
'''

'''
score = {'Korean':80, 'Math':90, 'English':70}
sum = 0
for i in score:
    sum += score[i]
print('평균=', sum/3.0)
'''

'''
english_dict = dict()
english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'
'''


'''
english_dict = {'one':'하나', 'two':'둘', 'three':'셋'}

word = input('단어를 입력하시오: ')
print(english_dict.get(word, '없음'))   
#.get( , ): 딕셔너리 안에 있으면 english_dict[word]가 출력되고 없으면 '없음'이 출력됨
#get함수를 더 많이 씀(에러 안떠서)
print(english_dict[word])   #없는걸 입력하면 에러뜸
'''


'''
#!!!!!!!!!!!!!!!!!!!!!!!엄청 중요한 문제!!!!!!!!!!!!!!!!!!!!!!!!!!!
frame = input('파일이름: ')
file = open(frame, 'r')

table = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1

print(table)
'''


'''
#p.29 축약어 풀어쓰기
#ppt보다 이 방법이 간단함
table = {'B4':'Before', 'TX':'Thanks', 'BBL':'Be Back Later', 'BCNU':'Be Seeing You'}

text = input('번역할 문장을 입력하시오: ')
words = text.split()
for i in words:
    if i in table:
        print(table[i], end=' ')
    else:
        print(i, end=' ')
'''


'''
#p.39 머리 글자어 만들기
a = input('문자열을 입력하시시오: ')

for word in a.upper().split():
    print(word[0], end='')
'''


'''
#p.41 이메일 주소 분석
address = input('이메일 주소를 입력하세요: ')
id, domain = address.split('@')    #앞에 변수는 두 개인데 @가 두개 나오면 3개로 쪼개지기 때문에 에러뜸
print('ID:', id)
print('Domain:', domain)
'''



'''
#p.42 문자열 분석
s = input('문자열을 입력하시오: ')
table = {'digits':0, 'spaces':0, 'alphas':0, 'dots':0}

for i in s:
    if i.isdigit():
        table['digits'] += 1
    elif i.isspace():
        table['spaces'] += 1
    elif i.isalpha():
        table['alphas'] += 1
    elif i == '.':
        table['dots'] += 1
        
print(table)
'''


'''
#8장 클래스와 객체
class sum:
    def a(self, ):  #클래스 안에서 함수(매소드)를 쓸 땐 첫번째 변수에 무조건 self적어줘야됨
        print('')
    def b(self, ):
        print('')
'''



'''
#p.8-11
class Counter:
    def reset(self):
        self.count = 0  #변수는 반드시 self.변수 써야됨
    def input(self, a):
        self.count = a
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
    def get(self):
        return self.count
    
a = Counter()
a.reset()
a.increment()
print(a.get())  #reset()안해주면 쓰레기 값이 들어있어서 에러남

b = Counter()
b.reset()
b.increment()
b.increment()
b.increment()
b.decrement()
print(b.get())

c = Counter()
c.input(100)
c.increment()
print(c.get())
'''


'''
#생성자
class Counter:
    def __init__(self, a):      #생성자 무조건 자동 호출
        self.count = a
    #변수 없을 땐
    #def __init__(self):
    #    self.count = 0  #0대신 다른 값 가능
    def reset(self):
        self.count = 0  #변수는 반드시 self.변수 써야됨
    def input(self, a):
        self.count = a
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
    def get(self):
        return self.count
    
a = Counter(100)
print(a.get())
'''

'''
#p.14 메소드 정의(테레비)
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        
    def show(self):
        print('채널:', self.channel, '볼륨:', self.volume, '상태', self.on)
    
    def showNoPrint(self):  #이 방법 쓰면 ()까지 같이 출력됨
        return self.channel, self.volume, self.on
    
    def setChannel(self, channel):
        self.channel = channel
    
    def setVolume(self, volume):
        self.volume = volume
        
    def sefOn(self, on):
        self.on = on
    
    def getChannel(self):
        return self.channel
    
    def getVolume(self):
        return self.volume
    
    def getOn(self):
        return self.volume
        
t = Television(10, 20, True)
#print(t.showNoPrint())     이렇게 쓰면 ()까지 같이 출력됨

t.show()
t.setChannel(50)
print(t.getChannel())
t.setVolume(100)
print(t.getVolume())
t.show()
'''

#변수 개수에 따라 settler와 gettler개수 똑같이 맞춰줘야됨

'''
class Television:
    def __init__(self, channel, volume, on):
        self.__channel = channel
        self.__volume = volume
        self.__on = on
        #뒤에 똑같은 함수다시 쓸때도 다 __붙여줘야됨
        
    def show(self):
        print('채널:', self.__channel, '볼륨:', self.__volume, '상태', self.__on)
    
    def setChannel(self, channel):
        self.__channel = channel
    
    def setVolume(self, volume):
        self.__volume = volume
        
    def sefOn(self, on):
        self.__on = on
    
    def getChannel(self):
        return self.__channel
    
    def getVolume(self):
        return self.__volume
    
    def getOn(self):
        return self.__volume

a = Television(30, 100, 1)
a.show()
print(a.getChannel())
'''

#self.__volume -> 정보 은닉