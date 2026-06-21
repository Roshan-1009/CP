def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # Grab the coins and convert them to integers
    coins = [int(x) for x in input_data[1:]]
    
    # 1. Sort the coins from smallest to largest
    coins.sort()
    
    # 2. Initialize the smallest impossible sum
    target = 1
    
    # 3. The Golden Rule Loop
    for coin in coins:
        if coin > target:
            # We found the gap! The game is over.
            break
            
        # The coin is small enough to help us. Stretch the boundary!
        target += coin
        
    print(target)  