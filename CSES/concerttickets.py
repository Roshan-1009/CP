def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = int(input_data[1])
    
    price = [0] + list(map(int, input_data[2:2+n]))
    price.sort()
    
    max_price = list(map(int, input_data[2+n:]))
    
    indexes = list(range(n+1))
    items = []
    
    def find(i):
        while i != indexes[i]:
            indexes[i] = indexes[indexes[i]]
            i = indexes[i]
        return i

    for current_price in max_price:
        index = bisect_right(price, current_price) - 1
        actual = find(index)
        
        if actual == 0:
            items.append("-1")
        else:
            items.append(str(price[actual]))
            indexes[actual] = find(actual - 1)
            
    print('\n'.join(items))