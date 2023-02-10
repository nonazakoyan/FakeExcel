import cell

class Spreadsheet:

    def __init__(self, row:int, col:int)->None:
        self.row = row
        self.col = col
        self.mCell = [[cell.Cell() for i in range(col)] for j in range(row)]

    def setCellAt(self, r:int, c:int, obj)->None:
        if r < 0 or r >= self.row or c < 0 or c >= self.col:
            print("Invaild input: ")
            return
        if type(obj) == str:
            self.mCell[r][c].getValue(obj)
        elif type(obj) == cell.Cell:
            self.mCell[r][c] = obj
        else:
            print("Obj type is incorrect: ")

    def getCellAt(self, r:int, c:int)->cell.Cell:
        return self.mCell[r][c]

    def addRow(self, row:int):
        self.mCell.insert(row, [cell.Cell() for i in range(self.col)])

    def removeRow(self, row:int):
        self.mCell.pop(row)

    def addColumn(self, col:int):
        for i in range(self.row):
            self.mCell[i].insert(col, cell.Cell())

    def removeColumn(self, col:int):
        for i in range(self.row):
            self.mCell[i].pop(col)

    def swapRows(self, x:int, y:int):
        self.mCell[x], self.mCell[y] = self.mCell[y], self.mCell[x]

    def swapColumns(self, x:int, y:int):
        for i in range(self.row):
            self.mCell[i][x], self.mCell[i][y] = self.mCell[i][y], self.mCell[i][x]