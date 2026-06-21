def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    size = int(input_data[0])
    products = int(input_data[1])
    list1=list(map(int, input_data[2:]))
    list1.sort()
    min_time=list1[0]
    max_time=min_time*products
    low=0
    high=max_time
    
    while low<=high:
        sum=0
        mid=(low+high)//2
        for machine in list1:
            sum+=(mid//machine)
        if sum<products:
            low=mid+1
        else:
            high=mid-1
    print(low)