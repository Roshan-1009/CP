def solve():
    y,x=map(int,input().split())#this splits the integers into list and maps into the following order
    m=max(x,y)
    if m%2==0:
        if x!=m:
            z=max(x,y)**2 - (x-1)#** is used as exponentiation operator
            print(z)
            return
        else:
            z=max(x,y)**2 - (2*(m-1)-(y-1))
            print(z)
            return
    else:
        if x!=m:
            z=max(x,y)**2 - (2*(m-1)-(x-1))
            print(z)
            return
        else:
            z=max(x,y)**2 - (y-1)
            print(z)
            return