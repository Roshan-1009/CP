def towr_of_honai(n,start,usage,destination):#hardcoding is fine,but the reucrsive function is atmost usable when the dynamic variables are being used
    # if n==2 and (start==1 and destination==2):#Every recursive function must have the base case at very top,not bottom because this gets checked first
    #     print(start,destination)#default comma is a space seperator
    #     print(start,usage)
    #     print(destination,start)
    #     print(usage,destination)
    #     print(start,destination)
    #     return#dont forget to return fromt he recursion
    # elif n==2 and (start==2 and destination==3):
    #     print(start,destination)#default comma is a space seperator
    #     print(start,usage)
    #     print(destination,start)
    #     print(usage,destination)
    #     print(start,destination)         
        # return #dont forget to return fromt he recursion
    if n==1:
         print(start,destination)
         return     
    towr_of_honai(n-1,start,destination,usage)
    print(start,destination)#default comma is a space seperator
    towr_of_honai(n-1,usage,start,destination)
def solve():
    disks = int(input().strip())
    if disks==0:
        print("No disks")
        return
    towr_of_honai(disks,1,2,3)
    #this function is 2^n exponential