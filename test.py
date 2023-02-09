import cell
import spreadsheet

class Test:

    def setValueTest(self, value):
        print(f"Result of run setValue() is {'passed' if cell.getValue(cell.setValue(value)) == value else 'Failed'}")

    def setColorTest(self, color):
        print(f"Result of run setColor() is {'passed' if cell.getColor(cell.setColor(color)) == color else 'Failed'}")

    def getValueTest(self):
        print(f"Result of run getValue is{ 'passed' if type(cell.getValue()) == str else 'Failed'}")

    def getColorTest(self):
        print(f"Result of run getColor() is {'passed' if type(cell.getColor()) == int else 'Failed'}")

    def toIntTest(self, cellObj):
        print(f"Result of run toInt() is {'passed' if cellObj.toInt() else 'Failed'}")

    def toDoubleTest(self, cellObj):
        print(f"Result of run toDouble() is {'passed' if cellObj.toDouble() else 'Failed'}")

    def toDateTest(self, cellObj):
        print(f"Result of run toDate() is {'passed' if cellObj.toDate() else 'Failed'}")

    def resetTest(self, cellObj):
        res = cellObj.reset()
        print(f"Result of run reset() is {'passed' if not(res.getValue or res.getColor) else 'Failes'}")