#----------5장-----------

'''
value = abs(-100)
print(value)
'''

'''
def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

a = get_sum(1, 10)
b = get_sum(1, 20)
print(a, b)
'''

'''
def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    print(start, '부터', end,'까지 더한 값은', sum)

get_sum(1, 10)
get_sum(1, 20)
'''

'''
def get_sum(x, y):
    sum = x + y
    return sum
    #return x + y

n1, n2 = input('숫자 두개를 넣으시오: ').split()
minNum = min(int(n1), int(n2))
maxNum = max(int(n1), int(n2))
get_sum(minNum, maxNum)
'''


'''
def main():
    n1, n2 = input('숫자 두개를 넣으시오: ').split()
    minNum = min(int(n1), int(n2))
    maxNum = max(int(n1), int(n2))
    get_sum(minNum, maxNum)
    
def get_sum(x, y):
    sum = x + y
    return sum

main()      #이 형태를 가장 많이 씀
'''

'''
def say_hello(name, msg):
    print('안녕', name, msg)

#say_hello('철수', '어서와')
#say_hello('길똥', '집에와')
name = input('이름을 넣어주세요: ')
msg = input('메세지를 넣어주세요: ')
say_hello(name, msg)
'''


def say_hello(name, msg):
    print('안녕', name, msg)

for i in range(3):
    name = input('이름을 넣어주세요: ')
    msg = input('메세지를 넣어주세요: ')
    say_hello(name, msg)
