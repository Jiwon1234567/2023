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
a.on = False
a.__volume = 200
a.show()