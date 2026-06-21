def solve():
    n=int(input().strip())
    datas=input()
    numbers=[int(x) for x in datas.split()]#take the data values and split into values and convert into int type and put in in numbers lsit,int(x),ot [x] 
    actual_sum=(n*(n+1))//2
    sum=0
    for i in numbers:
        sum=sum+i
    print(actual_sum-sum)