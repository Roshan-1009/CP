def solve():
    # Fast I/O to prevent Time Limit Exceeded (TLE)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = int(input_data[1])
    d = int(input_data[2])
    applicants=list(map(int,input_data[3:3+n]))
    apartments=list(map(int,input_data[3+n:]))#everything until the list ends
    apartments.sort()  
    applicants.sort()
    i=0
    j=0
    count=0
    while i<len(applicants) and j<len(apartments):
        limit=apartments[j]-applicants[i]
        if abs(limit)<=d:
            j+=1
            i+=1
            count+=1
        elif limit>0:
            i+=1
        elif limit<0:
            j+=1
    print(count)