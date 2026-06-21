from collections import deque
def solve():
    n=int(input().strip())
    board=[[-1]*n for _ in range(n)]#to check we only need to check the -1,otherwise we wont be able to differentiate the visiited nodes
    def bfs(initial_i,initial_j):
        queue=deque()
        visited=set()
        queue.append((initial_i,initial_j,0))#if i add dist also,then the same index will reappear multiple times with different indexes
        board[0][0]=0#if we dont assigned the inital value as 0,it wont get visited
        knightmoves=[(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(-2,-1),(2,-1),(-2,1)]
        while queue:#queue is not empty
             row,col,dist=queue.popleft()
             dist+=1
             for i,j in knightmoves:#Upper bound and lower bound must be given
                new_row=row+i#we need to add the knight moves to the particular grid,not kepp on adding all the knight moves
                new_col=col+j
                if 0<=row+i<n and 0<=col+j<n and board[new_row][new_col]==-1 :
                    board[new_row][new_col]=dist
                    queue.append((new_row,new_col,dist))
    bfs(0,0)
    for i in board:
         print(*i)
    return 