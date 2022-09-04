class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        total_row = len(board) - 1
        total_col = len(board[0]) - 1
        edge = []
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in [0,total_row] or j in [0,total_col]) and board[i][j] == 'O':
                    edge.append((i,j))
        vis = [[0]*total_col for i in range(total_row)]          
        while edge:
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            new_elm = []
            while edge:
                row,col = edge.pop(0)
                board[row][col] = "T"
                for dx,dy in dirs:
                    nr = row + dx
                    nc = col + dy
                    if 0 <= nr <= total_row and 0<= nc <= total_col:
                        if board[nr][nc] == "O":
                            board[nr][nc] = "T"
                            new_elm.append((nr,nc))   
            
            edge = new_elm.copy()  
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        
        return board