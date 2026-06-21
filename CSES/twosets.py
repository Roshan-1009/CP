def solve():
    n=int(input())
    sum=n*(n+1)//2
    if(sum%2!=0):
        print("NO")
        return
    else:
        print("YES")
        if n%2==0:
            print(n//2)
            for i in range(1,(n//4 + 1)):
                print(i,n+1-i,end=" ")
            print()    
            print(n//2)
            for i in range(n//4 + 1,n//2 + 1):
                print(i,n+1-i,end=" ")#Commas will already give you spaces    
        else:
            print((n-3)//2 + 2)
            print(1,2,end=" ")
            for i in range(4,(4 + (n-3)//4)):
                print(i,n-(i-4),end=" ")
            print()        
            print((n+3)//2 - 2)
            print(3,end=" ")
            for i in range(4 + (n-3)//4 ,4 + (n-3)//2):#Python does not let you add integers and strings together using a + sign. It will throw a TypeError.
                print(i,n-(i-4),end=" ")