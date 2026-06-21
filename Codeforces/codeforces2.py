import sys
import os

# 1. The Local Environment Check
if os.path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return 
        
    data = iter(input_data)
    
    try:
        t = int(next(data))
        
        # Loop through each test case
        for _ in range(t):
            n = int(next(data))
            k = int(next(data))
            binarystring = next(data)
            
            is_valid = True

            # Loop through each of the 'k' independent chains
            for j in range(k):
                # Slice the string to grab every k-th character starting from j
                chain = binarystring[j::k]
                
                # If any chain starts with an odd number of '1's, Arseniy cannot win
                if chain.count('1') % 2 != 0:
                    is_valid = False
                    break 
            
            # Print the result for this test case
            if is_valid:
                print('YES')
            else:
                print('NO')

    except StopIteration:
        pass

if __name__ == '__main__':
    solve()