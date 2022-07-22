import random
class yagoo:
    def __init__(self):
        self.randomAmount = 6
        self.randomValueA = random.randrange(0,self.randomAmount+1)
        self.randomValueB = random.randrange(0,self.randomAmount+1)
        self.randomValueC = random.randrange(0,self.randomAmount+1)
        self.randomList = [self.randomValueA,self.randomValueB,self.randomValueC]
    
    def games(self,valueList,randomList):

        if valueList[0] == randomList[0]:
            fir = 'strike'
        elif valueList[0] in randomList:
            fir = 'ball'
        else:
            fir = 'out'
        if valueList[1] == randomList[1]:
            sec = 'strike'
        elif valueList[1] in randomList:
            sec = 'ball'
        else:
            sec = 'out'
        if valueList[2] == randomList[2]:
            third = 'strike'
        elif valueList[2] in randomList:
            third = 'ball'
        else:
            third = 'out'
        return [fir,sec,third]
    def play(self):
        gameRandomValue = self.randomAmount
        for game in range(1,10):
            outputList = []
            for i in range(1,4):
                print ('aa 0~%s aa'%(gameRandomValue))
                inputSingle = int(input('%ss%ss :'%(game,i)))
                outputList.append(inputSingle)
            outputFilterList = self.games(outputList,self.randomList)
            print (self.randomList)
            strikeCount =  (outputFilterList.count('strike'))
            ballCount = (outputFilterList.count('ball'))
            outCount = (outputFilterList.count('out'))
            print (('%ssssss  ::  %sss / %s bbb / %s iooo')%(game,strikeCount,ballCount,outCount))
            if strikeCount == 3:
                print ('wwwwww')
                break
a = yagoo()
a.play()
