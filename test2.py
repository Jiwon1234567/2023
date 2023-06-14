from math import sqrt

def distance(a1, b1, a2, b2):
    distance = sqrt((int(a2) - int(a1)) ** 2 + (int(b2) - int(b1)) ** 2)
    return distance

x1, y1 = input('한점을 입력하세요: ').split()
x2, y2 = input('다른 한점을 입력하세요: ').split()

d = distance(x1, y1, x2, y2)
print('('+ x1 + ',' + y1 + ')과 (' + x2 + ',' + y2 + ')의 길이는 %f입니다.' %d)     #결과가 소수로 나올 수 있으므로 %f