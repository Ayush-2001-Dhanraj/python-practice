
def diagonalOrder(matrix, ROW, COL): 
    for line in range(1, (ROW + COL)): 

        start_col = max(0, line - ROW) 

        count = min(line, (COL - start_col), ROW) 

        for j in range(0, count): 
            print(matrix[min(ROW, line) - j - 1] 
                        [start_col + j], end="\t") 
  
        print() 
  


diagonalOrder([[1, 2, 3, 4 ,9 , 10], 
                 [5, 6, 7, 8, 12, 18], 
                 [9, 10, 11, 12, 32, 22], 
                 [13, 14, 15, 16, 16, 17], 
                 [17, 18, 19, 20, 22, 17]], 5 , 6)
