def solve():
    n=int(input().strip())
    datas=input()
    numbers=[int(x) for x in datas.split()]#take the data values and split into values and convert into int type and put in in numbers lsit,int(x),ot [x] 
    sortednum=sorted(numbers)
    if sortednum[0]!=1:
        print(1)
        return    
    for i in range(len(sortednum)-1):#for i in sortednum:--this i means the actual number in the list
        if sortednum[i+1]-sortednum[i]!=1:
            print(sortednum[i]+1)
            return#kill the function immediately after running