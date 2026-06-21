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
        
    # Create the iterator
    data = iter(input_data)
    
    try:
        # Grab the total number of test cases (e.g., 4)
        t = int(next(data))
        
        # Loop through each test case
        for _ in range(t):
            # 1. Grab 'n' for this specific test case
            n = int(next(data))
            
            # 2. Scoop out exactly 'n' elements for this test case's list
            list1 = [int(next(data)) for _ in range(n)]
            
            # 3. Your core logic
            maximum= max(list1)
            minimum = min(list1)
            subtraction = maximum - minimum + 1
            print(subtraction)
            
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()