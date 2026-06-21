def solve():
    n=int(input().strip())
    board=[[0]*n for _ in range(n)]#this creates n 0's as a string and add n strings of that
    for i in range(n):
         for j in range(n):
              board[i][j]=i^j#MEX OPERATION IS THE KEY BEHIND THIS QUESTION
    for k in board:#takes each string in board,which is ROW
         print(*k)#prints the entire row and newline for next row 