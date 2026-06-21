def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    numbers = [int(x) for x in input_data[1:]]
    i=0
    j=0
    myset=set()
    max=0
    count=0
    while i<=j and j<n:
        if numbers[j] not in myset:
            myset.add(numbers[j])
            count+=1
        else:
            myset.remove(numbers[i])
            i+=1
            count-=1
            continue       
        if count>max:
                max=count
        j+=1
    print(max) 