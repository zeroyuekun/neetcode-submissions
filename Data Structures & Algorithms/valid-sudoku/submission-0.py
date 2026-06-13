class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.validateLine(row):
                return False

        columns = self.getColumns(board)
        for column in columns:
            if not self.validateLine(column):
                return False

        boxes = self.getBoxes(board)
        for box in boxes:
            if not self.validateLine(box):
                return False
        return True

    def validateLine(self, sudokuLine: List[str]) -> bool:
        numSet = set()
        countOfNums = 0
        for i in range(len(sudokuLine)):
            if sudokuLine[i] != ".":
                numSet.add(sudokuLine[i])
                countOfNums+=1

        if len(numSet) == countOfNums:
            return True
        return False

    def getColumns(self, board: List[List[str]]):
        columns = []
        for colIdx in range(9):
            column = [board[rowIdx][colIdx] for rowIdx in range(9)]
            columns.append(column)
        return columns

    def getBoxes(self, board: List[List[str]]):
        boxes = []
        # we know that these boxes are 0, 1, 2 ... 3, 4, 5.. etc
        for boxRow in range(3):
            for boxCol in range(3):
                box = []
                for row in range(3):
                    for col in range(3):
                        actualRow = boxRow * 3 + row
                        actualCol = boxCol * 3 + col
                        box.append(board[actualRow][actualCol])
                boxes.append(box)
        
        return boxes
