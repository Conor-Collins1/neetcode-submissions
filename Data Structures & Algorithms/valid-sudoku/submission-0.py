class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for v, line in enumerate(board):
            seenH = [0]*10
            i = 0
            while i < 9:
                if line[i] != ".":
                    if seenH[int(line[i])] == 1:
                        return False
                    seenH[int(line[i])] = 1
                i += 1
            
            seenV = [0]*10
            for j in range(9):
                if board[j][v] != ".":
                    if seenV[int(board[j][v])] == 1:
                        return False
                    seenV[int(board[j][v])] = 1
            
        startY = 0
        for down in range(3):

            startX = 0

            for right in range(3):
                seenS = [0]*10

                for s in range(3):
                    
                    for i in range(3):
                        if board[s + startY][i + startX] != ".":
                                if seenS[int(board[s + startY][i + startX])] == 1:
                                    return False
                                seenS[int(board[s + startY][i + startX])] = 1
                startX += 3
            startY += 3
                

        return True
            
                 
                    


            

            

        

                
        