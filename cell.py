from datetime import datetime

class Cell():

    def __init__(self,value="", color=0) -> None:
        self.value = value
        self.color = color

    def setValue(self, value)->None:
        # value = str(value)
        self.value = value

    def setColor(self, color:int)->None:
        self.color = color

    def getValue(self):
        return self.value

    def getColor(self)->int:
        return self.color

    def toInt(self)->bool:
        #get Value
        value = self.getValue()
        #check is a valid convert?
        if type(value) == str and value.isdigit():
            self.getValue(int(value))
            return True
        return False

    def toDouble(self):
        value = self.getValue()
        if type(value) == type(str) and (ls := value.split('.')):
            for i in ls:
                if not i.isdigit():
                    return False
            self.getValue(float(value))
            return True
        return False

    def toDate(self):
        #valid format year-mounth-day
        format = "%Y-%m-%d %H:%M:%S"
        try:
            value = self.getValue() + " 00:00:00"
            date_time = datetime.strptime(value, format)
            self.getValue(date_time)
            return True
        except:
            return False

    def reset(self):
        self.value = ''
        self.color = 0