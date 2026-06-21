
   


def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    numbers = [int(x) for x in input_data[1:]]
    towertops=[]
    target=numbers[1]
    count=0
    for i in numbers:
        idx=bisect_right(towertops,i)
        if len(towertops)==idx:#last index which is physically not there,hence appending is needed
            towertops.append(i)
        else:    
            towertops[idx]=i
    print(len(towertops))