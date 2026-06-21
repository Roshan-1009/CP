def solve():
    n=int(input().strip())
    datas=input()
    numbers=[int(x) for x in datas.split()]
    moves=0
    for i in range(1,len(numbers)):#or instead of len(num) you can use n,which is len(num) tp avoid confusion
        if(numbers[i-1]>numbers[i]):#you can also runa a while loop until it satisfiesds ,but it is A RED FLAG,cause it increase complexity
            moves+=(numbers[i-1]-numbers[i])
            numbers[i]=numbers[i-1]#you didnt change the actual value oops,this is why you should take enough test cases
    print(moves)