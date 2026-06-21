def solve():
    # 1. Instantly read and convert all data to integers using C-level mapping
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 2. C-Level Slicing [start : stop : step]
    # We grab all arrivals (indexes 1, 3, 5...) and sort them instantly

    
    # We grab all departures (indexes 2, 4, 6...) and sort them instantly
    n=input_data[0]
    coins=sorted(list(map(int,input_data[1:])))
    sum=0
    natural=1
    for i in range(len(coins)):
        sum+=i
        if natural!=sum:
            print
        natural+=(i-1)


      