def solve():
    # Fast I/O to prevent Time Limit Exceeded (TLE)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    myset=set()
    for i in range(t):
        n=input_data[i+1]##since this integer or string identification was never an issue,we can use the string type also
        myset.add(n)
    print(len(myset))