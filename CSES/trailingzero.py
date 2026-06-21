def solve():
    n=int(input())    
    count=0
    while(n):
        n=n//5
        count+=n
    print(count) 