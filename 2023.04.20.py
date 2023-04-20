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


def get_sum(x, y):
    sum = x + y
    return sum
    #return x + y

n1, n2 = input('숫자 두개를 넣으시오: ').split()
minNum = min(int(n1), int(n2))
maxNum = max(int(n1), int(n2))
get_sum(minNum, maxNum)

