def solveBishops(n):
    
    posDiag = set()
    negDiag = set()
    board = [["."] * n for i in range(n)]
    res=[]

    def backtrack():
        
        for row in range(n):
            for column in range(n):
                if (row + column) in posDiag or (row-column) in negDiag:
                    continue

                posDiag.add(row+column)
                negDiag.add(row-column)
                board[row][column] = "B"

                backtrack()

                posDiag.remove(row+column)
                negDiag.remove(row-column)
                board[row][column] = '.'

                print("pos" , posDiag)
                print("neg" , negDiag)
                
        copy = ["".join(r) for r in board] # Getting an instance of the board and joining it with quotations
        res.append(copy)
        return
                
    backtrack()
    print(res)
    return res
print(solveBishops(4))



