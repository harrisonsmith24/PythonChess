
def solveQueens(n:int):
        col = set()
        posDiag = set() # (r+c)
        negDiag = set() # (r-c) # these are both sets to determine the diagonals for comparing the positions of the queens  "1+2=3 so that makes it the third diagonal"

        res = [] # Result/Solution
        board =[["."] * n for i in range(n)] # Defining of the board by setting the number of rows and columns to the passed in variable n

        def backtrack(r):
            if r==n: # If the row we are choosing to put a queen on is equal to the number that is being passed in as the dimmension for the board then we have reached the end and have found a spot of each queen.
                copy = ["".join(row) for row in board] # Getting an instance of the board and joining it with quotations
                res.append(copy)
                return

            for c in range(n): # testing every column (c) in the row 
                if c in col or (r+c) in posDiag or (r-c) in negDiag: # Checking to see if the position has already been used in the column, negative diagonal and positive diagonal
                    continue

            # add each of the sets to the board as being used
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."

                print("col" , col)
                print("pos" , posDiag)
                print("neg" , negDiag)
                print(res)
        backtrack(0)
        return res

print(solveQueens(4))