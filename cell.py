class Cell():

    def __init__(self,value="", color=0) -> None:
        self.value = value
        self.color = color

    def setValue(self, value:str)->None:
        #convert value to str!
        value = str(value)
        self.value = value

    def setColor(self, color:int)->None:
        self.color = color

    def getValue(self)->str:
        return self.value

    def getColor(self)->int:
        return self.color

    def toInt(self)->bool:
        #get Value
        #check is a valid convert?
        pass

    def toDouble(self):
        pass

    def toDate(self):
        pass

    def reset(self):
        pass