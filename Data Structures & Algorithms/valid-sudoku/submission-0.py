class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        for row in range(9):
            uniqueCheck={}
            for col in range(9):
                boardValue= board[row][col]
                if boardValue !='.':
                    if(boardValue not in uniqueCheck):
                        uniqueCheck[boardValue]=1
                    else:
                        return False
        for col in range(9):
            uniqueCheck={}
            for row in range(9):
                boardValue= board[row][col]
                if boardValue !='.':
                    if(boardValue not in uniqueCheck):
                        uniqueCheck[boardValue]=1
                    else:
                        return False
        for boxRow in range(0, 9, 3):
             for boxCol in range(0, 9, 3):
                uniqueCheck = {}
                for row in range(boxRow, boxRow + 3):
                     for col in range(boxCol, boxCol + 3):
                         boardValue = board[row][col]
                         if boardValue != '.':
                            if boardValue not in uniqueCheck:
                                uniqueCheck[boardValue] = 1
                            else:
                                return False
                        
       
        return True