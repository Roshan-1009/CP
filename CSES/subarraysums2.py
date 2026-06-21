def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    target = int(input_data[1])
    
    # 1. THE SHIELD: Generate a 64-bit random number the hacker cannot predict
    RANDOM_MASK = random.getrandbits(64)
    
    # 2. THE C-LEVEL DICT: defaultdict automatically handles missing keys
    sums = defaultdict(int)
    
    # Apply the shield to our base case!
    sums[0 ^ RANDOM_MASK] = 1
    
    count = 0
    current_sum = 0
    
    for num in map(int, input_data[2:]):
        current_sum += num
        
        # 3. Check Memory (Securely masked)
        difference = current_sum - target
        masked_diff = difference ^ RANDOM_MASK
        
        if masked_diff in sums:
            count += sums[masked_diff]
            
        # 4. Save to Memory (Securely masked)
        masked_sum = current_sum ^ RANDOM_MASK
        sums[masked_sum] += 1
        
    print(count)