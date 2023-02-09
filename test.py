import cell
import spreadsheet

class Test:
    def initCell(self):
        self.cell = cell.Cell()

    def setValueTest(self, value):
        print(f"Result of run setValue() is {'passed' if self.cell.getValue(self.cell.setValue(value)) == value else 'Failed'}")

    def setColorTest(self, color):
        print(f"Result of run setColor() is {'passed' if self.cell.getColor(self.cell.setColor(color)) == color else 'Failed'}")

    def getValueTest(self):
        print(f"Result of run getValue is{ 'passed' if type(self.cell.getValue()) == type(str) else 'Failed'}")

    def getColorTest(self):
        print(f"Result of run getColor() is {'passed' if type(self.cell.getColor()) == type(int) else 'Failed'}")

    def toIntTest(self, cellObj):
        print(f"Result of run toInt() is {'passed' if cellObj.toInt() else 'Failed'}")

    def toDoubleTest(self, cellObj):
        print(f"Result of run toDouble() is {'passed' if cellObj.toDouble() else 'Failed'}")

    def toDateTest(self, cellObj):
        print(f"Result of run toDate() is {'passed' if cellObj.toDate() else 'Failed'}")

    def resetTest(self, cellObj):
        res = cellObj.reset()
        print(f"Result of run reset() is {'passed' if not(res.getValue or res.getColor) else 'Failes'}")

    def initSpreadsheet(self, rows, columns):
        self.spreadsheet = spreadsheet.Spreadsheet(rows,columns)

    def setCellAtTest(self, r, c, obj):
        self.spreadsheet.setCellAt(r,c,obj)
        res = self.spreadsheet.getCellAt(r,c)
        if type(obj) == type(str):
            print(f"Result of run setCellAt() is {'passed' if res.getValue() == obj else'failed'}")
        else:
            print(f"Result of run setCellAt() is {'passed' if id(res) == id(obj) else'failed'}")

    def getCellAtTest(self, r, c):
        print(f"Result of run getCellAt() is {'passed' if self.spreadsheet.getCellAt(r,c) == type(self.cell()) else 'failes'}")

    def addRowTest(self, row):
        start = len(self.spreadsheet.mCell)
        self.spreadsheet.addRow(row)
        end = len(self.spreadsheet.mCell)
        print(f"Result of run addRow is {'passed' if end - start == 1 else 'failed'}")

    def removeRowTest(self, row):
        start = len(self.spreadsheet.mCell)
        self.spreadsheet.removeRow(row)
        end = len(self.spreadsheet.mCell)
        print(f"Result of run removeRow() is {'passed' if end - start == -1 else 'failed'}")

    def addColumnTest(self, col):
        start = len(self.spreadsheet.mCell[0])
        self.spreadsheet.addColumn(col)
        end = len(self.spreadsheet.mCell[0])
        print(f"Result of run addColumn() is {'passed' if end - start == 1 else 'failed'}")

    def removeColumnTest(self, col):
        start = len(self.spreadsheet.mCell[0])
        self.spreadsheet.removeColumn(col)
        end = len(self.spreadsheet.mCell[0])
        print(f"Result of run removeColumn() is {'passed' if end - start == -1 else 'failed'}")   


    def swapRowsTest(self, x, y):
        row1 = self.spreadsheet.mCell[x]
        row2 = self.spreadsheet.mCell[y]
        self.spreadsheet.swapRows(x, y)
        newrow1 = self.spreadsheet.mCell[y]
        newrow2 = self.spreadsheet.mCell[x]
        print(f"Result of run swapRows() {'passed' if (row1 == newrow1  and row2 == newrow2) else 'failed'}") 

    def swapColumnTest(self, x, y):
        col1 = [row[x] for row in self.spreadsheet.mCell]
        col2 = [row[y] for row in self.spreadsheet.mCell]
        self.spreadsheet.swapColumns(x, y)
        newcol1 = [row[y] for row in self.spreadsheet.mCell]
        newcol2 = [row[x] for row in self.spreadsheet.mCell]
        print(f"Result of run swapRows() {'passed' if (col1 == newcol1 and col2 == newcol2) else 'failed'}")


    # def runAllTests(self):
    #     self.setValueTest()
    #     self.setColorTest()
    #     self.getValueTest()
    #     self.getColorTest()
    #     self.toIntTest()
    #     self.toDoubleTest()
    #     self.toDateTest()
    #     self.resetTest()
    #     self.setCellAtTest()
    #     self.getCellAtTest()
    #     self.addRowTest()
    #     self.removeRowTest()
    #     self.addColumnTest()
    #     self.removeColumnTest()
    #     self.swapRowsTest()
    #     self.swapColumnTest()
