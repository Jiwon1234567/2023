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
        return self.on
        
t = Television(10, 20, True)
#print(t.showNoPrint())     이렇게 쓰면 ()까지 같이 출력됨

t.on = False

t.show()