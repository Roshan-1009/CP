def solve():
    s = int(input().strip()) 
    
    # Loop from 0 to (2^s - 1)
    for i in range(1 << s):
        # The Magic Formula: Convert standard integer 'i' to Gray Code integer
        gray = i ^ (i >> 1)#XOR operation 
        
        # Print it as a binary string, padded with leading zeros to length 's'
        print(f"{gray:0{s}b}")