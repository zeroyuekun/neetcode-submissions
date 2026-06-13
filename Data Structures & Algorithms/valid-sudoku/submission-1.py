class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Handle rows
        for row in board:
            if not self.isValidSegment(row):
                return False
        # Handle columns
        columns = self.getColumns(board)
        for col in columns:
            if not self.isValidSegment(col):
                return False

        # Handle boxes
        boxes = self.getBoxes(board)
        for box in boxes:
            if not self.isValidSegment(box):
                return False
        return True


    def isValidSegment(self, nums: List[str]):
        s = set()
        dupeCounter = 0
        for num in nums:
            if num != ".":
                s.add(num)
                dupeCounter+=1
        return len(s) == dupeCounter

    def getColumns(self, board: List[List[str]]) -> List[List[str]]:
        # board[0][0], board[1][0], board[2][0]
        columns = []
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            columns.append(column)
        return columns

    def getBoxes(self, board: List[List[str]]) -> List[List[str]]:
        # To get the first box..
        boxes = []
        for boxColSeg in range(3):
            for boxRowSeg in range(3):
                box = []
                for boxCol in range(3):
                    for boxRow in range(3):
                        boxColVal = boxColSeg * 3 + boxCol
                        boxRowVal = boxRowSeg * 3 + boxRow
                        box.append(board[boxColVal][boxRowVal])
                boxes.append(box)
        return boxes

                








