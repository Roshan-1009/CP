def solve():
      board=[]
      for _ in range(8):
            board.append(input().strip())
      #IN python a 2d array is automatically converted as needed
      #this will be a 2d arrray,with each item acting a row 
      cols=set()#set is uesed as same diagonals may overlap with each other
      diag1=set()
      diag2=set()
      count=0
      def backtrack(row):
            nonlocal count#this ensure that all recursion uses the smae count variable ,nonlocal notifies that to bring the count from outside
            if row==8:
                count+=1
                return
            for col in range(8):
                  if board[row][col]=='*': continue
                  if col in  cols: continue#for any row,if no cols enter it,then you wont enter backtrack(row+1),hence no furhter iteration
                  if row + col in diag1: continue #/ diagonal
                  if row - col in diag2: continue #\ diagonal
                  cols.add(col)#adding the restrictions for that speciic queen
                  diag1.add(row+col)
                  diag2.add(row-col)
                  backtrack(row+1)#keeping the queen as it is,go to the next row and keep a queen there
                  cols.remove(col)#in order to move to the next iteration(in the same row,different column),you need to remove the restrtiction for the queen you have kept now
                  diag1.remove(row+col)
                  diag2.remove(row-col)
      backtrack(0)
      print(count)
