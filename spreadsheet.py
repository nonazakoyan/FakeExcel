import cell
# from enum import Enum

# class Color(Enum):
#     WHITE = 0
#     RED = 1
#     GREEN = 2
#     BLUE = 3


class Spreadsheet:

    def __init__(self, row:int, col:int)->None:
        self.row = row
        self.col = col
        self.mCell = [[cell.Cell() for i in range(col)] for j in range(row)]

    def setCellAt(self, row:int, col:int, obj=None)->None:
        pass

    def getCellAt(self, row:int, col:int)->cell.Cell:
        pass

    def addRow(self, n:int):
        pass

    def removeRow(self, n:int):
        pass

    def addColumn(self, n:int):
        pass

    def removeColumn(self, n:int):
        pass

    def swapRows(self, x:int, y:int):
        pass

    def swapColumns(self, x:int, y:int):
        pass