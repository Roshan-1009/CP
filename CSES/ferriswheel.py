def solve():
    # Fast I/O to prevent Time Limit Exceeded (TLE)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = int(input_data[1])
    weights=list(map(int,input_data[2:]))
    weights.sort()
    t=a
    count=0
    i=0 
    j=len(weights)-1
    while i<=j:
        if a-weights[i]<0:
            break
        if a-weights[j]<0:
            j-=1
        if weights[i]+weights[j]<=a:
            count+=1
            i+=1
            j-=1
        else:
            count+=1
            j-=1
    print(count) 