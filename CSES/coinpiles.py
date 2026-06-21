def solve():
    a,b = map(int,input().split())
    z=max(a,b)
    x=min(a,b)
    if(x<0 or z<0):
        print("NO")
        return
    if(x==0 and z==0):
        print("YES")
        return    
    if z<=2*x  and (a+b)%3==0:#you should not avoid edge cases#to avoid runtime errors,you can convert division to multiplicaTION
        #you should not give contradictory condtions in or statment since it will always be true
        print("YES")
    else:
        print("NO")