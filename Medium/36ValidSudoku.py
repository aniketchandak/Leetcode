class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        l=set()
        for i in range (len(board)):
            # check col
                l.clear()
                for j in range (len (board)):

                    if board[i][j] in l:
                        return False
                    if board[i][j]!='.':
                        l.add(board[i][j])
               
                l.clear()
                #check row
                for j in range (len (board)):
                    if board[j][i] in l:
                        return False
                    if board[j][i]!='.':
                        l.add(board[j][i])
                print l
            
                
        #check box
        for k in range (len(board)):
                l.clear()
                for i in range (len(board)//3):
                    for j in range(len(board)//3): 
                        if board[((k//3)*3)+i][((k%3)*3)+j] in l:
                            return False
                        if board[((k//3)*3)+i][((k%3)*3)+j]!='.':  
                            l.add(board[((k//3)*3)+i][((k%3)*3)+j])
                print l
        return True
                        
            
        