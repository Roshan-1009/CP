def solve():
    n = int(input().strip())
    print(n,end="   ");    
    while(n!=1):
        if(n%2==0):
            n=n//2#never use / only for sivision,it will give float numbers only,to get integer numbers use double division operators
        else:
            n=n*3+1
        print(n,end="   "); 